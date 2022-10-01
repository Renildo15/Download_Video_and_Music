from pytube import YouTube
from pytube import Playlist
from tkinter import *
import moviepy.editor as mp
import re
import os
####################### funções########################################
def download_video():
    link = input('Digite o link do vídeo: ')
    path = input('Caminho de download: ')
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution().download(path)#Faz o download
    print("Download Completo")


