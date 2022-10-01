from pydoc import text
from tkinter import *
from funcoes import download_video
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os

#############################Interface#####################################

##################Configurações da janela##################################
janela = Tk()
janela.title("Software Download")
janela.resizable(False, False)
janela.iconbitmap("imgs/icon.ico")

largura = 750
altura = 520

largura_janela = janela.winfo_screenwidth()
altura_janela = janela.winfo_screenheight()

posx = largura_janela/2 - largura/2
posy = altura_janela/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

###########################Elementos da tela#################################
label_titulo = Label(janela, text="Baixar Música", font=("San-serif 25 bold"),pady=20)
label_link = Label(janela, text="Digite o link do vídeo:", font=("San-serif 20 bold"),pady=20)
entry_link = Entry(janela, width=40, font=("San-serif 20"))
entry_link.focus_set()

label_path = Label(janela, text="Caminho do download:", font=("San-serif 20 bold"), pady=20)
entry_path = Entry(janela, width=40, font=("San-serif 20"))

label_titulo.pack()
label_link.pack()
entry_link.pack()
label_path.pack()
entry_path.pack()


#########botao###############
def test():
    inp_link = entry_link.get()
    inp_path = entry_link.get()
    label_test.config(text = "Provided Input: "+inp_link)


def download_music():
    link = entry_link.get()
    path = entry_path.get()
    yt = YouTube(link)
    ys = yt.streams.filter(only_audio=True).first().download(path)

    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    label_test.config(text = "Download Completo", fg="green")




botao = Button(janela, text="Baixar", command=download_music, width=20, font="San-serif 15", bd=0, bg="red",cursor="star")
label_test = Label(janela, text="", font=("San-serif 20"), pady=20)
botao.pack()
label_test.pack()
#print(botao.keys()) Ver as propriedas



janela.mainloop()

