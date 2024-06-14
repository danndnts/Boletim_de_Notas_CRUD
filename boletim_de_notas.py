import tkinter as tk
from tkinter import messagebox#utilzar o messagebox ao inves de apenas imprimir 

#Função para criar o arquivo .txt
def criar_arquivo():
    with open("dados.txt", "w") as arquivo:# O modo "w" que se não e existir ele cria e se já houver uma com o mesmo nome ele remove
        arquivo.write("")# Uma string vazia dentro do arquivo


# Função para ler o arquivo .txt
def ler_arquivo():
    with open("dados.txt", "r") as arquivo:# O modo "r" significa que estamos abrindo para leitura, e o with para fecha-la assim que terminar de usar
        dados = arquivo.readlines()# readlines foi usado para ler todas as linhas do arquivo
        return dados# Retornamos a lista das linhas do arquivo para quem tenha chamado a funcao


# Função para inserir um registro no arquivo .txt
def inserir_registro():
    nome = entrada_nome.get()# Como estamos usando o tkinter, o .get() ele "pega" o valor de uma entrada, no caso uma Entry
    idade = entrada_idade.get()
    sexo = entrada_sexo.get()
    matricula = entrada_matricula.get()
    nota1 = entrada_nota1.get()
    nota2 = entrada_nota2.get()
    nota3 = entrada_nota3.get()# Pegando os valores das variáveis "entrada_nome", "entrada_idade", etc. E essas variáveis vem da entrada da interface do tkinter
    media = ( float(nota1) + float(nota2) + float(nota3)) / 3 #Calculando a média das notas
    media = round(media, 2) # Arredondando a média para duas casas decimais
    dados = [nome, idade, sexo, matricula, nota1, nota2, nota3, media] # Criando uma lista com as informacoes coletadas
    with open("dados.txt", "a") as arquivo: # O modo "a" serve para indicar que ANEXARÁ dados ao final do arquivo existente sem apagar o conteúdo
        arquivo.write("\n" + ",".join([str(elemento) for elemento in dados])) # Concatena todos os dados do arquivo em uma string para salvar no arquivo
    messagebox.showinfo("Sucesso", "Registro inserido com sucesso!")# Mesma funcao do print, modificado para se tornar de uma maneira mais amigavel, ao inves de so escrever no terminal

# Função para atualizar um registro no arquivo .txt
def atualizar_registro():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    sexo = entrada_sexo.get()
    matricula = entrada_matricula.get()
    nota1 = entrada_nota1.get()
    nota2 = entrada_nota2.get()
    nota3 = entrada_nota3.get()
    if not nota1 or not nota2 or not nota3: #Checa se alguma das notas está vazia
        messagebox.showerror("Erro", "As notas devem ser inseridas.")
        return
    media = (float(nota1) + float(nota2) + float(nota3)) / 3
    media = round(media, 2)
    dados = ler_arquivo() #Lê todas as linhas do arquivo "dados.txt"
    for i in range(len(dados)):
        linha = dados[i].strip() # .strip para ignorar todos os espacos desnecessários
        if linha.startswith(matricula):
            dados[i] = f"{nome},{idade},{sexo},{matricula},{nota1},{nota2},{nota3},{media}\n"
    with open("dados.txt", "w") as arquivo:
        arquivo.writelines(dados)# Abre o arquivo e escreve a mundancas salvas no dados.txt
    messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")

# Função para excluir um registro no arquivo .txt
def excluir_registro():
    var_matricula_excluir = entrada_matricula.get()# Pega o valor armazenado na entrada e armazena na variável var_matricula_excluir
    if not var_matricula_excluir:
        messagebox.showerror("Erro", "Por favor, informe a matrícula a ser excluída.")# Caso não seja preenchida aparecerá esse erro
        return
    try:# Tenta executar as instrucoes do bloco de código
        with open("dados.txt", "r") as arquivo:# Abre no modo leitura
            dados = arquivo.readlines()# Lê as linhas do arquivo
        with open("dados.txt", "w") as arquivo:# Abre o arquivo no modo escrita
            for i in dados:# Loop para verificar todas as linhas do arquivo
                elementos = i.split(",")# Divide a linha i usando virgula como separador e armazena na lista elementos
                if len(elementos) >= 4:
                    matricula = elementos[3].strip()# Pega o quarto elemento da lista e retira todos os espacos em branco
                    if matricula != var_matricula_excluir:
                        arquivo.write(i)# Escreve alinha i no arquivo para manter as outras matrículas que não queremos excluir
        messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")
    except FileNotFoundError:# Excecao se o arquivo não for encontrado 
        messagebox.showerror("Erro", "Nenhum registro encontrado.")


# Função para exibir os registros do arquivo .txt
def exibir_registros(): #define uma função
    dados = ler_arquivo()
    registros = "\n".join([linha.strip() for linha in dados if linha.strip()])# Percorre cada linha em dados, remove os espaços em branco no início e no final de cada linha usando strip(); \n.join transforma toda  lista em uma sting só e separa por quebras de linhas.
    messagebox.showinfo("Registros", registros if registros else "Nenhum registro encontrado.")


# Inicializando a interface gráfica
#def_main ( ): 
criar_arquivo ( ) 
janela = tk.Tk ( ) #instância da biblioteca tkinter
janela.title ("CRUD BOLETIM") #o title é um atributo usado para definir o título da janela. 
janela.geometry ("400x400")#definindo o tamanho

# Criando rótulos (labels) e campos de entrada
tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky='e')# Labels adicionadas para uma melhor organizacao do texto
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Idade:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Sexo:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entrada_sexo = tk.Entry(janela)
entrada_sexo.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Matrícula:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entrada_matricula = tk.Entry(janela)
entrada_matricula.grid(row=3, column=1, padx=10, pady=5)

tk.Label(janela, text="Nota 1:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
entrada_nota1 = tk.Entry(janela)
entrada_nota1.grid(row=4, column=1, padx=10, pady=5)

tk.Label(janela, text="Nota 2:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
entrada_nota2 = tk.Entry(janela)
entrada_nota2.grid(row=5, column=1, padx=10, pady=5)

tk.Label(janela, text="Nota 3:").grid(row=6, column=0, padx=10, pady=5, sticky='e')
entrada_nota3 = tk.Entry(janela)
entrada_nota3.grid(row=6, column=1, padx=10, pady=5)

# Criando os botões
botao_criar = tk.Button(janela, text="Inserir", command=inserir_registro)
botao_criar.grid(row=7, column=0, columnspan=2, pady=10)

botao_ler = tk.Button(janela, text="Procurar", command=exibir_registros)
botao_ler.grid(row=8, column=0, columnspan=2, pady=10)

botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_registro)
botao_atualizar.grid(row=9, column=0, columnspan=2, pady=10)

botao_excluir = tk.Button(janela, text="Excluir Matrícula", command=excluir_registro)
botao_excluir.grid(row=10, column=0, columnspan=2, pady=10)

# Chamando a função mainloop()
janela.mainloop()