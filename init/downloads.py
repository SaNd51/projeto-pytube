from pytube import Playlist, YouTube
from tkinter import * # type: ignore
from tkinter import ttk
from converter import *
import os, re

class tela:
    def __init__(self):
        self.janela = Tk()
        self.janela.iconbitmap(r'ico/play.ico')
        self.janela.title("Pytube")
        self.janela.geometry("400x340")
        self.janela.configure(bg="#9C2520")
        self.janela.resizable(width=FALSE, height=FALSE)
    pass


p = os.getcwd() 
janela = tela().janela
color = ["#2F4F4F", "#9C1520", "#B0E0E6", "#1B20D6"]
s = ttk.Style().configure('barra', background=color[0], foreground=color[0], thickness=40)
b = DoubleVar()
b.set(0)

def caminho():    
    r = p + '\\music'      
    if not os.path.exists(r):
        os.mkdir(r)        
    return r

os.chdir(caminho())

def baixar_P(videos):  
    print('Downloads: ' + videos.title)
    videos.streams.filter(progressive=True).order_by('resolution').desc().first().download(caminho())
       
def baixar_V(yt):
    print('Download: ' + yt.title)
    yt.download(caminho())
       
def f1(link,n,x):              
    l = ttk.Progressbar(janela, style=s, variable=b, maximum=n)
    l.place(width=200, height=20, x=100, y=250)
    yt = YouTube(
        'http://youtube.com/watch?v=2lAe1cqCOXo',
        use_oauth=False,
        allow_oauth_cache=True
    )
    yt = yt.streams.get_highest_resolution()
    baixar_V(yt)
    b.set(x)
    janela.update()

    def cria_pasta():
        new_folder = caminho() + '\\video\\'
        if not os.path.exists(new_folder): os.mkdir(new_folder) 
        return new_folder
    
    for file in os.listdir():
        if re.search(r'\.mp4$',file):           
            os.rename(file, cria_pasta() + file)
          
def f2(link):   
    p = Playlist(link)
    x,cont = len(p.video_urls), 0
    for videos in p.videos:
        l = ttk.Progressbar(janela, style=s, variable=b, maximum=100)
        l.place(width=200, height=20, x=100, y=250)
        baixar_P(videos)
        cont += 1
        n = (cont/x)*100
        b.set(n)
        janela.update()
            
    l = list(p.title)
    for i in l:
        if i == (('/') or  (':') or ('|')):l.remove(i) 
    l = ''.join(map(str, l)); pasta = f'{l}\\'
                         
    def cria_pasta():
        folder = caminho() + '\\playlist\\'         
        if not os.path.exists(folder): os.mkdir(folder)    
        new_folder = folder + pasta
        if not os.path.exists(new_folder): os.mkdir(new_folder) 
                
        return new_folder
                    
    for file in os.listdir():
        if re.search(r'\.mp4$',file): os.rename(file, cria_pasta() + file)
        print(f'Movendo arquivo "{file}"')
    