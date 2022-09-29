from importlib.resources import path
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os


def download_video():
    link = input('Digite o link do vídeo: ')
    path = input('Caminho de download: ')
    yt = YouTube(link)
    ys = yt.streams.filter(only_audio=True).first().download(path)#Faz o download
    print("Download Completo")

def download_music():
    link = input('Digite o link do video: ')
    path = input('Caminho do download: ')
    yt = YouTube(link)
    ys = yt.streams.filter(only_audio=True).first().download(path)

    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print("Download Completo")

download_music()