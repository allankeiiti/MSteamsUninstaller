from win32net import NetUserEnum
from time import sleep
from win32netcon import FILTER_NORMAL_ACCOUNT
from getpass import getuser
from os import system
from tkinter import *

def listusers(server=None):
    # Essa função recolhe o nome de todos os perfis de usuário da estação
    # Source: # https://stackoverflow.com/questions/41018572/how-to-know-which-all-users-have-a-account
    level = 0
    filter = FILTER_NORMAL_ACCOUNT
    resume_handle = 0
    # Declara uma lista de usuário
    user_list = []
    while True:
        result = NetUserEnum(server, level, filter, resume_handle)
        user_list += [user['name'] for user in result[0]]
        resume_handle = result[2]
        if not resume_handle:
            break
    # Ordena a lista de usuários
    user_list.sort()
    return user_list

def taskkill(hostDestino):
    # Essa função encerra o processo da estação
    print(var.get())
    #system("psexec \\{} taskkill /im teams.exe /f".format(hostDestino))

def teamsUninstall(hostDestino, listUsers):
    # Função que executa o comando para desinstalar o Teams
    for user in listUsers:
        comando = r"\\{}\c$\Users\{}\AppData\Local\Microsoft\Teams\Update.exe --uninstall".format(hostDestino, user)
        system(comando)
        print(var.get())

print('Bem Vindo')
sleep(0)

listaUsuarios = listusers()
# Adquire o usuário que está utilizando o computador, para a mensagem de Bem Vindo
usuario = getuser()
janela = Tk()
# Colocando a janela para não ser redimencionável na vertical e horizontal
janela.resizable(False, False)
# Configurando Dimensões
janela.geometry("300x300")
# Colocando título
janela.title("TekkaKnight | ML Gomes")

# Foto de fundo
fundo = PhotoImage(file = "bg.png")
labelbg = Label(janela, image = fundo)
labelbg.place(x = 0, y = 0, relwidth = 1, relheight = 1)

boasVindasMsg = Label(janela, text ="Bem Vindo {}.".format(usuario), fg ="white",
                          bg = "blue", font = ("arial", 12, "bold"))

var = StringVar()
# Criando campo de texto (Host Destino)
hostDestino = Entry(janela, textvariable = var)
hostDestino.place(x = 75, y = 100)


# Criando botão de Iniciar
iniciarBtn = Button(janela, text = "Iniciar", fg = "white", bg = "blue", relief = GROOVE,
                    font = ("arial", 12, "bold"),
                    command = taskkill(var))
iniciarBtn.place(x = 75, y = 200)

# Criando botão de Fechar
fecharBtn = Button(janela, text = "Fechar", fg = "white", bg = "red", relief = GROOVE,
                   font = ("arial", 12, "bold"), command = exit)
fecharBtn.place(x = 150, y = 200)

boasVindasMsg.pack()
# Exibe a Janela para o usuário
janela.mainloop()

list = listusers()
for user in list:
    print(user)

