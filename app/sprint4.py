# import funcoes
# import json


# clientes = []
# menu = 0
# med = False



# while menu == 0:
#     option = int(input("1- Deseja fazer o login? \n2- Deseja fazer o cadastro?\n"))

#     if option == 1:
#         email = input("Digite seu email: ")
#         senha = input("Digite sua senha: ")

#         acesso_permitido, nome_usuario, usuario_id = funcoes.verificar_login_senha(email, senha)

#         if acesso_permitido:
#             print(f"\nAcesso permitido! Bem-vindo, {nome_usuario}!\n")
#             menu = 1
#         else:
#             print(f"\nAcesso negado: {nome_usuario}\n\n")
    
#     elif option == 2:
#         print("Bem-vindo! Por favor, faça o seu registro!\n")
#         nome = input("Por favor, informe seu nome:\n")
#         email = input("Digite o e-mail:\n")
#         cep = input("Informe seu CEP (formato xxxxx-xxx):\n")
#         senha = input("Digite sua senha!\n")
#         senha2 = input("Confirme sua senha!\n")
#         tipo_usuario = input("Você é um médico? (S para sim, qualquer outra tecla para não): ").lower()
#         if tipo_usuario == "s":
#             med = True
#         #chama a function que valida as informações e faz as devidas checagens
#         if funcoes.validar_informacoes(nome, cep, email):
#             if senha != senha2 :
#                 print("Por favor, verifique as informações e tente novamente.")
#             else:
#                 print("Informações válidas. Registro concluído!")
#                 print("Faça o login!\n\n")
#                 funcoes.clientes_global(clientes, nome, email, cep, senha,med)
#                 option = 1 #Abre o menu principal




# #Menu principal
# while menu == 1 :
#     if funcoes.verificar_medico == False:
#         print(f"\n\n------Bem vindo a nossa Homepage {nome_usuario}!,Quais dos serviços disponiveis você deseja acessar------")
        
#         #Se o usuário é medico ou paciente
#         # if funcoes.verificaProduto(usuario_id):

#         option = int(input("\n\n1-Desejo salvar as leituras em meu Illtracker e salvar algum sintoma \n2-Desejo Fazer Log-Out do app\n"))

#         if option == 1:
#                 menu = funcoes.illtrackerP(nome_usuario)
            
#         elif option == 2:
#             menu = 2
#     elif funcoes.verificar_medico == True:
#             option2 = int(input("\n\n1-Desejo verificar o historico de um paciente\n2-Desejo efetuar o logout\n\n"))
#             if option2 == 1:
#                  nome_paciente = input("Digite o nome do paciente: ")
#                  funcoes.historico_medico(nome_paciente)      

import funcoes
import json

clientes = []
menu = 0
med = False
nome_usuario = None  # Adicione esta linha

while menu == 0:
    option = int(input("1- Deseja fazer o login? \n2- Deseja fazer o cadastro?\n"))

    if option == 1:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        acesso_permitido, nome_usuario, usuario_id = funcoes.verificar_login_senha(email, senha)

        if acesso_permitido:
            print(f"\nAcesso permitido! Bem-vindo, {nome_usuario}!\n")
            menu = 1
        else:
            print(f"\nAcesso negado: {nome_usuario}\n\n")
    
    elif option == 2:
        print("Bem-vindo! Por favor, faça o seu registro!\n")
        nome = input("Por favor, informe seu nome:\n")
        email = input("Digite o e-mail:\n")
        cep = input("Informe seu CEP (formato xxxxx-xxx):\n")
        senha = input("Digite sua senha!\n")
        senha2 = input("Confirme sua senha!\n")
        tipo_usuario = input("Você é um médico? (S para sim, qualquer outra tecla para não): ").lower()
        if tipo_usuario == "s":
            med = True
        #chama a function que valida as informações e faz as devidas checagens
        if funcoes.validar_informacoes(nome, cep, email):
            if senha != senha2 :
                print("Por favor, verifique as informações e tente novamente.")
            else:
                print("Informações válidas. Registro concluído!")
                print("Faça o login!\n\n")
                funcoes.clientes_global(clientes, nome, email, cep, senha, med)
                menu = 1  # Corrija esta linha para atribuir 1 diretamente à variável 'menu'

# Menu principal
while menu == 1:
    if not funcoes.verificar_medico(nome_usuario):  # Adicione 'not' aqui para verificar se o usuário NÃO é médico
        print(f"\n\n------Bem vindo a nossa Homepage {nome_usuario}!, Quais dos serviços disponíveis você deseja acessar------")
        
        # Se o usuário é médico ou paciente
        # if funcoes.verificaProduto(usuario_id):
        option = int(input("\n\n1-Desejo salvar as leituras em meu Illtracker e salvar algum sintoma \n2-Desejo Fazer Log-Out do app\n"))

        if option == 1:
                menu = funcoes.illtrackerP(nome_usuario)
        elif option == 2:
            menu = 2
    elif funcoes.verificar_medico(nome_usuario):  # Adicione 'nome_usuario' como argumento aqui
        option2 = int(input("\n\n1-Desejo verificar o histórico de um paciente\n2-Desejo efetuar o logout\n\n"))
        if option2 == 1:
            nome_paciente = input("Digite o nome do paciente: ")
            funcoes.historico_medico(nome_paciente)
            escolha = int(input("\nDeseja voltar ao menu principal (digite 1) ou fazer o Log-Out (digite 2)? "))
        
            if escolha == 1:
                menu = 1
            else:
                menu = 2 
