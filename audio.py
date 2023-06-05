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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
