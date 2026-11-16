import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QBoxLayout,QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtCore import Qt,QTime,QTimer

class Stop_watch(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        self.setMinimumSize(320, 200)
        self.time=QTime(0,0,0,0)
        self.timer=QTimer(self)
        self.time_label=QLabel("00:00:00:00",self)
        self.button_start=QPushButton("Start",self)
        self.button_stop=QPushButton("Stop",self)
        self.button_reset=QPushButton("Reset",self)
        self.button_start.clicked.connect(self.start_timer)
        self.button_stop.clicked.connect(self.stop_timer)
        self.button_reset.clicked.connect(self.reset_timer)
        self.timer.timeout.connect(self.update_time)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Stop Watch")
        self.setStyleSheet("background-color:black;")
        self.time_label.setStyleSheet("""
            QLabel {
                background-color: #1e293b;
                color: #f8fafc;
                font-size: 52px;
                font-weight: bold;
                border: 2px solid #475569;
                border-radius: 12px;
                padding: 10px;
            }
        """)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setMinimumHeight(120)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(18)
        layout.addWidget(self.time_label, stretch=1)
        layout.addLayout(self.buttons())
        self.setLayout(layout)

    def buttons(self):
        button_style = """
            QPushButton {
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 18px;
                font-size: 16px;
                min-width: 80px;
            }
            QPushButton:hover { border: 1px solid white; }
            QPushButton:pressed { padding-top: 12px; padding-bottom: 8px; }
        """
        self.button_start.setStyleSheet(button_style + "QPushButton { background-color: #28a745; }")
        self.button_stop.setStyleSheet(button_style + "QPushButton { background-color: #dc3545; }")
        self.button_reset.setStyleSheet(button_style + "QPushButton { background-color: #6c757d; }")

        hbox = QHBoxLayout()
        hbox.setSpacing(12)
        hbox.addWidget(self.button_start)
        hbox.addWidget(self.button_stop)
        hbox.addWidget(self.button_reset)
        return hbox

        
    def start_timer(self):
        self.timer.start(10)

    def stop_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self,time):
        hours=time.hour()
        min=time.minute()
        sec=time.second()
        msec=time.msec() // 10
        return f"{hours:02}:{min:02}:{sec:02}:{msec:02}"

    def update_time(self):
        self.time=self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__=="__main__":
    app=QApplication(sys.argv)
    stop_watch=Stop_watch()
    stop_watch.show()
    sys.exit(app.exec_())
