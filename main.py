import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navigation System Simulator")
        self.setFixedSize(700, 400)
        icon = QIcon("source/pin.png")
        self.setWindowIcon(icon)

        self.button_click_sound = QSoundEffect()
        self.button_click_sound.setSource(QUrl.fromLocalFile("source/pi.wav"))

        self.create_webview()
        self.create_buttons()
        self.create_labels()

    def create_webview(self):
        self.webview = WebView(self)

    def create_buttons(self):
        off_button = QPushButton(self)
        off_button.setGeometry(88, 350, 82, 48)
        off_button.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        off_button.clicked.connect(self.off_button_click)
        off_button.setIcon(QIcon("source/off.png"))
        off_button.setIconSize(off_button.size())
        off_button.raise_()

        on_button = QPushButton(self)
        on_button.setGeometry(5, 350, 82, 48)
        on_button.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        on_button.clicked.connect(self.on_button_click)
        on_button.setIcon(QIcon("source/on.png"))
        on_button.setIconSize(on_button.size())
        on_button.hide()  # 初めは非表示
        on_button.raise_()

        button2 = QPushButton(self)
        button2.setGeometry(5, 350, 82, 48)
        button2.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button2.clicked.connect(self.button_click)
        button2.setIcon(QIcon("source/shousai.png"))
        button2.setIconSize(button2.size())
        button2.raise_()

        button3 = QPushButton(self)
        button3.setGeometry(615, 350, 82, 48)
        button3.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button3.clicked.connect(self.button_click)
        button3.setIcon(QIcon("source/koiki.png"))
        button3.setIconSize(button3.size())
        button3.raise_()

        button4 = QPushButton(self)
        button4.setGeometry(245, 350, 131, 48)
        button4.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button4.clicked.connect(self.button_click)
        button4.setIcon(QIcon("source/hyoujihenkou.png"))
        button4.setIconSize(QSize(131, 48))
        button4.setFixedSize(131, 48)
        button4.raise_()

        button5 = QPushButton(self)
        button5.setGeometry(480, 350, 131, 48)
        button5.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        button5.clicked.connect(self.button_click)
        button5.setIcon(QIcon("source/titentouroku.png"))
        button5.setIconSize(QSize(131, 48))
        button5.setFixedSize(131, 48)
        button5.raise_()

        self.buttons = [off_button, on_button, button2, button3, button4, button5]  # ボタンをリストで保持

    def create_labels(self):
        label1 = QLabel(self)
        label1.setGeometry(0, 0, 96, 61)
        label1.setPixmap(QPixmap("source/houi.png"))
        label1.raise_()

        label2 = QLabel(self)
        label2.setGeometry(0, 60, 93, 58)
        label2.setPixmap(QPixmap("source/gps.png"))
        label2.raise_()

        label3 = QLabel(self)
        label3.setGeometry(0, 120, 93, 42)
        label3.setPixmap(QPixmap("source/vics.png"))
        label3.raise_()

        label4 = QLabel(self)
        label4.setGeometry(460, -5, 243, 30)
        label4.setPixmap(QPixmap("source/etc.png"))
        label4.raise_()

    def create_webview(self):
        webview = WebView(self)

    def button_click(self):
        self.button_click_sound.play()

    def off_button_click(self):
        self.buttons[0].hide()  # offボタン非表示
        self.buttons[1].show()  # onボタン表示
        for button in self.buttons[2:]:  # 他のボタン非表示
            button.hide()
        self.button_click_sound.play()

    def on_button_click(self):
        self.buttons[0].show()  # offボタン表示
        self.buttons[1].hide()  # onボタン非表示
        for button in self.buttons[2:]:  # 他のボタン表示
            button.show()
        self.button_click_sound.play()

class WebView(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(0, -50, 800, 500)
        self.load(QUrl("https://map.yahoo.co.jp/?lat=35.70345&lon=139.74911&zoom=17&maptype=traffic"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())