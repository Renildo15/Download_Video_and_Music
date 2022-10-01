from tkinter import *
from funcoes import download_music, download_video

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
label_titulo = Label(janela, text="Baixar Música", font=("San-serif 25 bold"))
label_link = Label(janela, text="Digite o link do vídeo:", font=("San-serif 20 bold"))
entry_link = Entry(janela, width=40)
entry_link.focus_set()

label_path = Label(janela, text="Caminho do download:", font=("San-serif 20 bold"))
entry_path = Entry(janela, width=40)

label_titulo.pack()
label_link.pack()
entry_link.pack()
label_path.pack()
entry_path.pack()


#########botao###############
def test(msg):
    print(msg)
botao = Button(janela, text="Baixar", command=lambda:test("Opa"), width=20, font="San-serif 15 bold", bd=0, bg="red")
botao.pack()



janela.mainloop()

