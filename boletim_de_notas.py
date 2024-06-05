import tkinter as tk

def criar_arquivo():#Funcao para criar os arquivos.
    with open("dados.txt", "w") as arquivo:#o modo "w" que se não e existir ele cria e se já houver uma com o mesmo nome ele remove
        arquivo.write("")#Uma string vazia dentro do arquivo