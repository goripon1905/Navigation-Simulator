import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon, QFont, QColor
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl, QSize, QTimer, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navigation System Simulator")
        self.setFixedSize(700, 400)
        icon = QIcon("source/pin.png")
        self.setWindowIcon(icon)

        self.button_click_sound = QSoundEffect()
        self.button_click_sound.setSource(QUrl.fromLocalFile("source/pi.wav"))


        # audio_menu.pngを表示
        bkg = QPushButton(self)
        bkg.setGeometry(0, 0, 700, 400)
        bkg.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        bkg.setIcon(QIcon("source/menu.png"))
        bkg.setIconSize(bkg.size())
        bkg.raise_()

        # メニュー名ラベル
        label = QLabel("オーディオソース選択", self)
        label.setGeometry(15, 10, 200, 30)
        font1 = QFont("Meiryo", 15)
        label.setFont(font1)
        color = QColor("aqua")
        label.setStyleSheet("color: {}".format(color.name()))

        # ボタン配置
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
        button7.clicked.connect(self.info1_click)
        button7.setIcon(QIcon("source/USB.png"))
        button7.setIconSize(button7.size())
        button7.raise_()

        self.info_label = QLabel(self)
        self.info_label.setGeometry(0, 0, 700, 400)
        self.info_label.setScaledContents(True)
        self.info_label.hide()

        self.text_label = QLabel(self)
        self.text_label.setGeometry(145, 190, 1000, 20)
        self.text_label.setText("接続されたUSBデバイスは対応していません")
        self.font2 = QFont("Meiryo", 15, QFont.Bold)
        self.text_label.setFont(self.font2)
        self.text_label.setStyleSheet("color: white")
        self.text_label.hide()


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hide_info_label)

    def info1_click(self):
        self.button_click_sound.play()
        self.info_label.setPixmap(QPixmap("source/info1.png"))
        self.info_label.show()
        self.text_label.show()
        self.timer.start(3000)  # 3秒間表示する

    def hide_info_label(self):
        self.info_label.hide()
        self.text_label.hide()
        self.timer.stop()

    def button_click(self):
        self.button_click_sound.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
