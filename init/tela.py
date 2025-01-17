from turtle import color
from gerenciar import *
from converter import main_loop
from tkinter import * # type: ignore

linha = Label(janela, text="Download do link",background=color[1], foreground=color[2])
linha.place(width=200, height=20, x=100, y=100)

bt_1 = Button(janela, text="adicionar", bd=0.5, activebackground=color[3], activeforeground=color[2], command=lambda: adicionar(
link.get()), background=color[1], foreground=color[2])
bt_1.place(width=80, height=20, x=100, y=150)

bt_2 = Button(janela, text="converter", bd=0.5, activebackground=color[3],activeforeground=color[2], command=main_loop, background=color[1], foreground=color[2])
bt_2.place(width=80, height=20, x=220, y=150)

bt_3 = Button(janela, text="baixar", bd=0.5, activebackground=color[3], activeforeground=color[2],command=lambda: baixar(link.get()), background=color[1], foreground=color[2],justify=CENTER)
bt_3.place(width=80, height=20, x=158, y=180)

janela.mainloop()
