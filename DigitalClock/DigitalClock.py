from PyQt5.QtWidgets import QWidget,QLabel,QApplication,QBoxLayout,QVBoxLayout
from PyQt5.QtCore import Qt, QTime,QTimer
from PyQt5.QtGui import QFont,QFontDatabase
import sys

class Digital_Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label= QLabel(self)
        self.timer=QTimer()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,400,100)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("font-size:100px;""font-family=Arial;""background-color:black;""color:lightgreen;")
        time_font=QFontDatabase.addApplicationFont("DS-DIGII.TTF")
        timer_font=QFontDatabase.applicationFontFamilies(time_font)[0]
        fonts=QFont(timer_font,150)
        self.time_label.setFont(fonts)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)


        self.update_time()

    def update_time(self):
        timer_update=QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(timer_update)

if __name__=="__main__":
    app=QApplication(sys.argv)
    Clock=Digital_Clock()
    Clock.show()
    sys.exit(app.exec_())
    