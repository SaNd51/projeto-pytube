import re
import os

main_folder = os.getcwd() + '\\'
os.chdir(main_folder)  
#print(os.listdir())

def lista(file):
    file_name, file_extension = os.path.splitext(file)
    
    if not file_name:
        return file 
    
    l = []
    for file in os.listdir():
        if re.search(file_extension, file):
           l = file_extension       
    return l

def dup():
    l_1 = []
    l_2 = []
    for file in os.listdir():
        l_1.append(lista(file))
    dup = [x for i, x in enumerate(l_1) if i == l_1.index(x)]
    
    for f in dup:
        l = list(f)
        for i in l:
            if i == '.':     
                l.remove(i)
        x = ''.join(map(str, l))
        l_2.append(x) 
       
    return l_2

a = dup() 
     
def cria_pasta():  
    new_folder = []
    l1 = []
    
    for i in range(len(a)):
        l1 = main_folder + '\\' + a[i]
        new_folder.append(l1)     
        if not os.path.exists(new_folder[i]):
            os.mkdir(new_folder[i]) 
    return new_folder

def mover(): 
    #print(a)        
    for i in range(len(a)):
        for f in os.listdir(main_folder):            
            if f != 'move-arquivo.exe':                           
                if lista(f) == ('.' + a[i]):
                    os.rename(f, cria_pasta()[i] + '\\'  + f ) 
                    #print(cria_pasta()[i] + '\\' + f)
                    #print(f)
            l = list(f)
            l = [x for i, x in enumerate(l) if i != '.']
            #print(l)
    print('Operação concluida')
                
mover()
                         
           


      
      
