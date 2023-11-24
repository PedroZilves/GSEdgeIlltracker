import json
import re
import conexao

# Função para verificar o login e a senha
def verificar_login_senha(email, senha):
    with open('db.json', 'r', encoding='utf-8') as f:
        clientes = json.load(f)
        for cliente in clientes['clientes']:
            if cliente['email'] == email:
                if cliente['senha'] == senha:
                    return True, cliente['nome'], cliente['id']
                else:
                    return False, "Senha incorreta", None

        return False, "Usuário inexistente", None
    









#Recebe dados do json e atualiza com novo cliente
def clientes_global(clientes, nome, email, cep, senha,med):
    try:
        with open('db.json', 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:  # Verifica se o conteúdo do arquivo está vazio
                clientes = {'clientes':[]}
            else:
                f.seek(0)  # Volta para o início do arquivo
                clientes = json.load(f)
    
    except FileNotFoundError:
        clientes = {'clientes':[]}

    cliente_id = len(clientes['clientes']) + 1  # Gere um ID único
    cliente = {
        'id': cliente_id,
        'nome': nome,
        'email': email,
        'cep': cep,
        'senha': senha,
        'medico': med
        
    }

    clientes['clientes'].append(cliente)


    with open('db.json', 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)





#Function para validar as informações obtidas do cliente
def validar_informacoes(nome, cep, email):
    if not re.match("^[a-zA-Z\s\w~]*$", nome, re.UNICODE):
        print("Nome só pode conter letras")
        return False
    if not re.match("^\d{5}-\d{3}$", cep):
        print("CEP deve ser composto de 5 dígitos, um traço e 3 dígitos")
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("O e-mail está inválido")
        return False
    return True







#Status do Clean Drain
def illtrackerP(nome):
    print("\n\nUltima leitura do sensor")

    conexao.conexao_Arduino()

    with open('db.json', 'r', encoding='utf-8') as f:
        illTracker = json.load(f)
    
    bpm = illTracker['illTracker']['heartrate']
    temp = illTracker['illTracker']['temperature']
    data = illTracker['illTracker']['dataHora']
    print(f"\n\nRegistrado  \n• {bpm} batimentos por minutos\n• {temp} graus celcius de temperatura")
    print(f"Data e hora da última checagem: {data}")

    adicionar_sintoma = input("\nDeseja adicionar sintomas? (S para sim, qualquer outra tecla para não): ").lower()

    if adicionar_sintoma == 's':
        nome_usuario = nome

        sintomas = input("Digite os sintomas (separados por vírgula): ")
        sintomas = sintomas.split(',')

        registro_sintomas = {
            'nome_usuario': nome_usuario,
            'data_hora': data,
            'sintomas': sintomas
        }

        salvar_sintomas(registro_sintomas)
    
    escolha = int(input("\nDeseja voltar ao menu principal (digite 1) ou fazer o Log-Out (digite 2)? "))
        
    if escolha == 1:
        menu = 1
    else:
        menu = 2 
    
    return menu

def salvar_sintomas(registro_sintomas):
    try:
        with open('db.json', 'r', encoding='utf-8') as f:
            sintomas_data = json.load(f)
    except FileNotFoundError:
        sintomas_data = {'registros': []}

    sintomas_data['registros'].append(registro_sintomas)

    with open('db.json', 'w', encoding='utf-8') as f:
        json.dump(sintomas_data, f, indent=4, ensure_ascii=False)
    
def historico_medico(nome_paciente):
    with open('db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    registros_paciente = [registro for registro in data.get("registros", []) if registro.get("nome_usuario") == nome_paciente]

    if registros_paciente:
        print(f"Histórico de sintomas para o paciente {nome_paciente}:")
        for registro in registros_paciente:
            print(f"Data e hora: {registro.get('data_hora')}")
            print(f"Sintomas: {', '.join(registro.get('sintomas', []))}")
            print("\n---\n")
    else:
        print(f"Nenhum histórico encontrado para o paciente {nome_paciente}.")


    return registros_paciente
def verificar_medico(nome_usuario):
    with open('db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for cliente in data.get("clientes", []):
        if cliente.get("nome") == nome_usuario and cliente.get("medico"):
            return True
    return False
