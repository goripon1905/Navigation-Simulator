import tkinter as tk
from PIL import ImageTk, Image
import pygame

# ウィンドウの作成
window = tk.Tk()
window.geometry("700x400")
window.title("Navigation System Simulator")

# 画像の読み込み
koiki_path = "source/koiki.png"
koiki = Image.open(koiki_path)

shousai_path = "source/shousai.png"
shousai = Image.open(shousai_path)

off_path = "source/off.png"
off = Image.open(off_path)

hyoujihenkou_path = "source/hyoujihenkou.png"
hyoujihenkou = Image.open(hyoujihenkou_path)

titentouroku_path = "source/titentouroku.png"
titentouroku = Image.open(titentouroku_path)

houi_path = "source/houi.png"
houi = Image.open(houi_path)

gps_path = "source/gps.png"
gps = Image.open(gps_path)

vics_path = "source/vics.png"
vics = Image.open(vics_path)

etc_path = "source/etc.png"
etc = Image.open(etc_path)

pin_path = "source/pin.png"
pin = Image.open(pin_path)

# pygameの初期化
pygame.mixer.init()

# クリック時の処理
def button_click():
    pygame.mixer.music.load("source/pi.wav")
    pygame.mixer.music.play()

# 画像ボタンの表示
photo = ImageTk.PhotoImage(koiki)
button = tk.Button(window, text="", image=photo, command=button_click)
button.place(x=615, y=350)

photo2 = ImageTk.PhotoImage(shousai)
button2 = tk.Button(window, text="", image=photo2, command=button_click)
button2.place(x=0, y=350)

photo3 = ImageTk.PhotoImage(off)
button3 = tk.Button(window, text="", image=photo3, command=button_click)
button3.place(x=88, y=350)

photo4 = ImageTk.PhotoImage(hyoujihenkou)
button4 = tk.Button(window, text="", image=photo4, command=button_click)
button4.place(x=245, y=350)

photo5 = ImageTk.PhotoImage(titentouroku)
button5 = tk.Button(window, text="", image=photo5, command=button_click)
button5.place(x=480, y=350)

photo6 = ImageTk.PhotoImage(houi)
button6 = tk.Label(window, text="", image=photo6)
button6.place(x=0, y=0)

photo7 = ImageTk.PhotoImage(gps)
button7 = tk.Label(window, text="", image=photo7)
button7.place(x=0, y=60)

photo8 = ImageTk.PhotoImage(vics)
button8 = tk.Label(window, text="", image=photo8)
button8.place(x=0, y=120)

photo9 = ImageTk.PhotoImage(etc)
button9 = tk.Label(window, text="", image=photo9)
button9.place(x=460, y=-5)


window.mainloop()