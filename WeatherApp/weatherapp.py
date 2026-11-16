import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


weather_api = "Paste The API KEY here"


class WeatherWorker(QThread):
    weather_ready = pyqtSignal(dict)
    error_occurred = pyqtSignal(str)

    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        try:
            weather_data = fetch_weather_data(self.city)
            self.weather_ready.emit(weather_data)
        except (ValueError, HTTPError, URLError, TimeoutError) as error:
            self.error_occurred.emit(str(error))


def fetch_weather_data(city):
    if not weather_api or weather_api == "Paste The API KEY here":  # Do NOT add the API KEY in this line!!!
        raise ValueError("Add the API key!")

    request_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={weather_api}&units=metric"
    )
    with urlopen(request_url, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))

    return {
        "city": data["name"],
        "temperature": round(data["main"]["temp"]),
        "condition": data["weather"][0]["description"].capitalize(),
        "condition_id": data["weather"][0]["id"],
    }


def get_weather_emoji(condition_id):
    if condition_id == 800:
        return "☀️"
    if 801 <= condition_id <= 804:
        return "☁️"
    if 700 <= condition_id < 800:
        return "🌫️"
    if 600 <= condition_id < 700:
        return "❄️"
    if 500 <= condition_id < 600:
        return "🌧️"
    if 300 <= condition_id < 400:
        return "🌦️"
    if 200 <= condition_id < 300:
        return "⛈️"
    return "🌤️"


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = None
        self.setWindowTitle("Weather App")
        self.setMinimumWidth(360)
        self.setMinimumHeight(300)
        self.build_ui()

    def build_ui(self):
        self.city_input = QLineEdit()
        self.city_input.setObjectName("cityInput")
        self.status_label = QLabel("Enter a city to see its weather:")
        self.status_label.setObjectName("status")
        self.status_label.setWordWrap(True)
        
        self.city_input.setPlaceholderText("(e.g. London)")
        self.city_input.returnPressed.connect(self.on_search_clicked)

        self.search_button = QPushButton("Get Weather")
        self.search_button.setObjectName("searchButton")
        self.search_button.clicked.connect(self.on_search_clicked)

        self.emoji_label = QLabel("🌤️")
        self.emoji_label.setStyleSheet("font-size: 56px;")
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setObjectName("weatherEmoji")

        self.temperature_label = QLabel("Temperature: --°C")
        self.temperature_label.setStyleSheet("font-weight:bold;font-size:18px;margin-top:10px")
        self.condition_label = QLabel(" Cloud condition: --")
        self.condition_label.setStyleSheet("font-weight:bold;font-size:18px")
        self.condition_label.setObjectName("condition")

        layout = QVBoxLayout()
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(12)
        layout.addWidget(self.status_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.emoji_label, 1)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.condition_label)
        

        container = QWidget()
        container.setObjectName("weatherPage")
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setStyleSheet("""
            QWidget#weatherPage { background: #eef4fb; color: #172b4d; }
            QLineEdit#cityInput {
                background: white; border: 1px solid #cbd8e6; border-radius: 10px;
                padding: 10px 12px; color: #172b4d;
            }
            QLineEdit#cityInput:focus { border: 2px solid #3478c7; }
            QPushButton#searchButton {
                background: #2672c9; color: white; border: 0; border-radius: 10px;
                padding: 11px; font-weight: 700;
            }
            QPushButton#searchButton:hover { background: #1d5fae; }
            QPushButton#searchButton:disabled { background: #9bb9d9; }
            QLabel#weatherEmoji { color: #183b66; }
            QLabel#condition { color: #60758e; font-weight: 700; }
            QLabel#status { color: #172b4d; font-weight: 700; }
        """)
        self.resize(460, 440)
        self.update_responsive_sizes()


    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_responsive_sizes()

    def update_responsive_sizes(self):
        scale = min(self.width() / 420, self.height() / 440)
        scale = max(0.75, min(scale, 1.6))

        self.emoji_label.setFont(QFont(self.font().family(), round(56 * scale)))
        self.temperature_label.setFont(
            QFont(self.font().family(), round(18 * scale), QFont.Bold)
        )
        self.condition_label.setFont(
            QFont(self.font().family(), round(18 * scale), QFont.Bold)
        )
        self.status_label.setFont(
            QFont(self.font().family(), round(18 * scale), QFont.Bold)
        )
        self.city_input.setMinimumHeight(round(34 * scale))
        self.search_button.setMinimumHeight(round(36 * scale))

    def on_search_clicked(self):
        city = self.city_input.text().strip()
        if not city:
            self.show_error("Please enter a city name.")
            return

        self.search_button.setEnabled(False)
        self.status_label.setText("Loading weather…")
        self.worker = WeatherWorker(city)
        self.worker.weather_ready.connect(self.display_weather)
        self.worker.error_occurred.connect(self.show_error)
        self.worker.finished.connect(lambda: self.search_button.setEnabled(True))
        self.worker.start()

    def display_weather(self, weather):
        self.setWindowTitle(f"Weather — {weather['city']}")
        self.temperature_label.setText(f"Temperature: {weather['temperature']}°C")
        self.condition_label.setText(f"Cloud condition: {weather['condition']}")
        self.emoji_label.setText(get_weather_emoji(weather["condition_id"]))
        self.status_label.setText("")

    def show_error(self, message):
        self.status_label.setText(f"Could not get weather: {message}")


def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
