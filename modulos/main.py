from tkinter import *
from funcoes import download_video, download_music
from janela_music import abrir_janela
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os

janela_principal = Tk()
janela_principal .title("Software Download")
janela_principal .resizable(False, False)
janela_principal .iconbitmap("imgs/icon.ico")



largura = 750
altura = 320

largura_janela = janela_principal .winfo_screenwidth()
altura_janela =janela_principal .winfo_screenheight()

posx = largura_janela/2 - largura/2
posy = altura_janela/2 - altura/2

janela_principal.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))



label_titulo = Label(janela_principal, text="Software Download", font=("San-serif 25 bold"),pady=20)
botao_music = Button(janela_principal, text="Musica", command = abrir_janela, width=20, font="San-serif 15", bd=0, bg="red",cursor="star")
botao_video = Button(janela_principal, text="Video", width=20, font="San-serif 15", bd=0, bg="red",cursor="star")



label_titulo.pack()
botao_music.pack()
botao_video.pack()
janela_principal.mainloop()