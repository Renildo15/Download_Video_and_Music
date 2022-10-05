from pytube import YouTube
from pytube import Playlist
from tkinter import *
import moviepy.editor as mp
import re
import os
####################### funções########################################
def download_video(link_video, path_video, label_test):
    link = link_video.get()
    path = path_video.get()
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution().download(path)#Faz o download
    label_test.config(text = "Download Completo", fg="green")

def download_music(link_music, path_music, label_test):
    link = link_music.get()
    path = path_music.get()
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

