from tkinter import * # type: ignore
from urllib.parse import urlparse, parse_qs
from downloads import *
import time

class mostrar:
    def __init__(self, texto):
        self.texto = texto
    pass

urls = []
link = Entry(janela, bd=1, font=("Calibri", 10), justify=CENTER)
link.place(width=200, height=20, x=100, y=120)

def bt(text):
    texto = f'{text:.30}'
    l = mostrar(texto)
    t = Label(janela, text='',  background=color[0],foreground="#90EE90", borderwidth=0, justify=CENTER)
    t['text'] = l.texto
    t.place(width=200, height=20, x=100, y=250)

def query(url,cont):
    n = len(urls)
    if urlparse(url).query:

        p = parse_qs(urlparse(url).query)
        for f in p.popitem(): 
            if type(f) == str: 
                if f == 'list': f2(url); 
            else: f1(url,n,cont+1)      

        time.sleep(0.5)
        janela.update()
        bt('Download concluído')

def baixar(url):
    cont = 0
    adicionar(url)
    for i in urls: query(i,cont); cont+=1
    urls.clear()
        
def adicionar(url):
    if len(url) == 0: bt('Copie um link')
    elif not urlparse(url).query: bt('Isso não é um link')
    else: 
        if not url in urls: urls.append(url); bt('adicionou: ' + url)
    link.delete(0, END)
