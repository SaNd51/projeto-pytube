from tkinter import *  # type: ignore
from urllib.parse import urlparse
from downloads import *  # type: ignore
import time


class mostrar:
    def __init__(self, texto):
        self.texto = texto


urls = []
link = Entry(janela, bd=1, font=("Calibri", 10), justify=CENTER)
link.place(width=200, height=20, x=100, y=120)


def bt(text):
    texto = f'{text:.30}'
    l = mostrar(texto)
    t = Label(janela, text='', background=color[0], foreground="#90EE90", borderwidth=0, justify=CENTER)
    t['text'] = l.texto
    t.place(width=200, height=20, x=100, y=250)


def query(url, cont):
    if not urlparse(url).query:
        bt('Isso não é um link')
        return

    bt('Baixando...')
    f1(url, 1, cont + 1)
    time.sleep(0.5)
    janela.update_idletasks()
    bt('Download concluído')


def baixar(url):
    adicionar(url)
    for index, item in enumerate(urls.copy()):
        query(item, index)
    urls.clear()


def adicionar(url):
    if len(url) == 0:
        bt('Copie um link')
    elif not urlparse(url).query:
        bt('Isso não é um link')
    else:
        if url not in urls:
            urls.append(url)
            bt('adicionou: ' + url)
    link.delete(0, END)
