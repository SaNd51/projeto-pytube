from yt_dlp import YoutubeDL  # type: ignore
from tkinter import *  # type: ignore
from tkinter import ttk
from converter import *
import os
import re


class tela:
    def __init__(self):
        self.janela = Tk()
        self.janela.iconbitmap(r'ico/play.ico')
        self.janela.title("Pytube")
        self.janela.geometry("400x340")
        self.janela.configure(bg="#9C2520")
        self.janela.resizable(width=FALSE, height=FALSE)


p = os.getcwd()
janela = tela().janela
color = ["#2F4F4F", "#9C1520", "#B0E0E6", "#1B20D6"]
ttk.Style().configure('barra', background=color[0], foreground=color[0], thickness=40)
b = DoubleVar()
b.set(0)


def caminho():
    r = os.path.join(p, 'music')
    if not os.path.exists(r):
        os.makedirs(r, exist_ok=True)
    return r


os.chdir(caminho())


def baixar_V(url):
    print('Download: ' + url)
    opcoes = {
        'outtmpl': os.path.join(caminho(), '%(title)s.%(ext)s'),
        'format': 'best',
        'quiet': True,
        'noplaylist': True,
    }

    with YoutubeDL(opcoes) as ydl:  # type: ignore
        ydl.download([url])


def f1(link, n, x):
    l = ttk.Progressbar(janela, style='TProgressbar', variable=b, maximum=max(1, n))
    l.place(width=200, height=20, x=100, y=250)

    baixar_V(link)

    b.set(x)
    janela.update()

    def cria_pasta():
        new_folder = os.path.join(caminho(), 'video')
        if not os.path.exists(new_folder):
            os.makedirs(new_folder, exist_ok=True)
        return new_folder

    for file in os.listdir(caminho()):
        if re.search(r'\.mp4$', file):
            os.rename(
                os.path.join(caminho(), file),
                os.path.join(cria_pasta(), file)
            )
          
    