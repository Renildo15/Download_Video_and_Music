from tkinter import *
from funcoes import download_music, download_video

#############################Interface#####################################

janela = Tk()

janela.geometry("750x520")
janela.title("Software Download")
janela.resizable(False, False)
janela.iconbitmap("imgs/icon.ico")

label_link = Label(janela, text="Digite o link do vídeo:", font=("Courier 12 bold"))
entry_link = Entry(janela, width=40)
label_link.grid(row=0, column=6)
entry_link.grid(row=1, column=6)
entry_link.focus_set()

label_path = Label(janela, text="Caminho do download:", font=("Courier 12 bold"))
entry_path = Entry(janela, width=40)
label_path.grid(row=2, column=6)
entry_path.grid(row=3, column=3)


#########botao###############
def test(msg):
    print(msg)
botao = Button(janela, text="Baixar", command=lambda:test("Opa"))
botao.grid(row=4, column=6)



janela.mainloop()

