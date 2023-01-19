from pytube import Playlist, YouTube
import os, re

def caminho():
    path = os.getcwd()   
    r = path + '\\music'      
    if not os.path.exists(r):
        os.mkdir(r)        
    return r

cd = caminho()
os.chdir(cd)

def baixar_P(videos):  
    print('Downloads: ' + videos.title)
    videos.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(cd)
    #mostrar(videos.title)  
    #tela().att  
       
def baixar_V(yt):
    print('Download: ' + yt.title)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(cd)
    #mostrar(yt.title)
    
def f1(link):              
    yt = YouTube(link)
    #print(yt)
    baixar_V(yt)
    
    def cria_pasta():
        new_folder = cd + '\\video\\'
        if not os.path.exists(new_folder):
            os.mkdir(new_folder) 
        return new_folder
    
    for file in os.listdir():
        if re.search(r'\.mp4$',file):           
            os.rename(file, cria_pasta() + file)
          
def f2(link):   
    p = Playlist(link)
    
    for videos in p.videos:
        baixar_P(videos)
            
    l = list(p.title)
    for i in l:
        if i ==  (('/') or  (':') or ('|')):
            l.remove(i) 
    l = ''.join(map(str, l))
    pasta = f'{l}\\'
                         
    def cria_pasta():
        folder = cd + '\\playlist\\'         
        if not os.path.exists(folder):
            os.mkdir(folder)
            
        new_folder = folder + pasta
        if not os.path.exists(new_folder):
            os.mkdir(new_folder) 
                
        return new_folder
                    
    for file in os.listdir():
        if re.search(r'\.mp4$',file):           
            os.rename(file, cria_pasta() + file)
        print(f'Movendo arquivo "{file}"')
    