from urllib.parse import urlparse, parse_qs
from tkinter import * 
from tkinter import ttk
from utils import main_loop
from main import f1, f2
import time

class mostrar:
    def __init__(self, texto):
        self.texto = texto
    pass

class tela:
    def __init__(self):
        self.janela = Tk()      
        self.janela.title("Pytube")
        self.janela.geometry("400x340")
        self.janela.configure(background='#4B0082')
        self.janela.resizable(width=FALSE, height=FALSE)    
    pass
    
urls = []
janela = tela().janela
s = ttk.Style().configure('barra', background='#2F4F4F', foreground= "#2F4F4F", thickness= 40)


linha = Label(janela, text = "Download do link", background='#8A2BE2', foreground= "#B0E0E6")
linha.place(width= 200, height=20, x = 100, y = 100)
link = Entry(janela, bd=1, font=("Calibri", 10), justify= CENTER)
link.place(width= 200, height=20, x = 100, y = 120)

bt_1 = Button(janela, text="adicionar", bd=0.5, activebackground= '#DA70D6', activeforeground='#B0E0E6', command = lambda: adicionar(link.get()), background='#8A2BE2', foreground= "#B0E0E6")
bt_1.place(width= 80, height=20, x=100, y=150)



bt_2 = Button(janela, text="converter", bd=0.5, activebackground= '#DA70D6', activeforeground='#B0E0E6', command = main_loop, background='#8A2BE2', foreground= "#B0E0E6")
bt_2.place(width= 80, height=20, x=220, y=150)

b = DoubleVar()        
b.set(0)

def bt(text):
    texto = f'{text:.30}'
    l = mostrar(texto)
    t = Label(janela, text= '',  background='#2F4F4F', foreground= "#90EE90", borderwidth= 0, justify=CENTER)   
    t['text'] = l.texto
    t.place(width= 200, height=20, x=100, y= 250)

def query(url,n):
    
    if urlparse(url).query:
        l = ttk.Progressbar(janela, style= s , variable= b , maximum= len(urls))
        l.place(width= 200, height=20, x=100, y=250)
        
        p = parse_qs(urlparse(url).query) 
        b.set(n/2) 
                  
        for f in p.popitem():
            if type(f) == str:
                if f == 'list':
                    f2(url)                    
                else: 
                                           
                    f1(url)
        b.set(n)
        janela.update() 
        time.sleep(0.5)   
        bt('Download concluído')
        
        
def baixar(url): 
    n = 0
   
    if len(urls) > 0:          
        for i in urls: 
            n+=1           
            query(i,n)                                                                 
    else:
        n = 1
        query(url,n)
            
    link.delete(0,END)     
        
def adicionar(url):
    
    if len(url) == 0:
        bt('Copie um link')
    elif not urlparse(url).query:
        bt('Isso não é um link')        
    else:  
        if not url in urls: 
            urls.append(url) 
        bt('Download: ' + url)
        
    link.delete(0,END)
                 
bt_3 = Button(janela, text="baixar", bd=0.5, activebackground= '#DA70D6', activeforeground='#B0E0E6', command = lambda: baixar(link.get()) , background='#8A2BE2', foreground= "#B0E0E6")
bt_3.place(width= 80, height=20, x=158, y=180)

janela.mainloop()