import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl, QSize, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navigation System Simulator")
        self.setFixedSize(700, 400)
        icon = QIcon("source/pin.png")
        self.setWindowIcon(icon)

        self.button_click_sound = QSoundEffect()
        self.button_click_sound.setSource(QUrl.fromLocalFile("source/pi.wav"))


#audio_menu.pngを表示
        bkg = QPushButton(self)
        bkg.setGeometry(0, 0, 700, 400)
        bkg.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        bkg.setIcon(QIcon("source/audio_menu.png"))
        bkg.setIconSize(bkg.size())
        bkg.raise_()

        button1 = QPushButton(self)
        button1.setGeometry(110, 100, 112, 112)
        button1.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button1.clicked.connect(self.button_click)
        button1.setIcon(QIcon("source/AM.png"))
        button1.setIconSize(button1.size())
        button1.raise_()

        button2 = QPushButton(self)
        button2.setGeometry(230, 100, 112, 112)
        button2.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button2.clicked.connect(self.button_click)
        button2.setIcon(QIcon("source/FM.png"))
        button2.setIconSize(button2.size())
        button2.raise_()

        button3 = QPushButton(self)
        button3.setGeometry(350, 100, 112, 112)
        button3.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button3.setIcon(QIcon("source/DISC.png"))
        button3.setIconSize(button1.size())
        button3.raise_()

        button4 = QPushButton(self)
        button4.setGeometry(470, 100, 112, 112)
        button4.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button4.clicked.connect(self.button_click)
        button4.setIcon(QIcon("source/SD.png"))
        button4.setIconSize(button4.size())
        button4.raise_()

        button5 = QPushButton(self)
        button5.setGeometry(110, 220, 112, 112)
        button5.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button5.clicked.connect(self.button_click)
        button5.setIcon(QIcon("source/TV.png"))
        button5.setIconSize(button5.size())
        button5.raise_()

        button6 = QPushButton(self)
        button6.setGeometry(230, 220, 112, 112)
        button6.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button6.clicked.connect(self.button_click)
        button6.setIcon(QIcon("source/Bluetooth.png"))
        button6.setIconSize(button6.size())
        button6.raise_()

        button7 = QPushButton(self)
        button7.setGeometry(350, 220, 112, 112)
        button7.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button7.clicked.connect(self.button_click)
        button7.setIcon(QIcon("source/USB.png"))
        button7.setIconSize(button7.size())
        button7.raise_()

    def button_click(self):
        self.button_click_sound.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
