# Assistente Virtual HC - Sistema de Apoio para Teleconsultas

pacientes = []  # Lista para armazenar os pacientes cadastrados
presencas = []  # Lista para confirmar presença

# Função para validar CPF

def validar_cpf(cpf):
    if len(cpf) == 11 and cpf.isdigit():
        return True
    return False

# Função para validar idade

def validar_idade(idade):
    if idade.isdigit():
        return True
    return False

# Função para cadastrar paciente
def cadastrar_paciente():
    print("\n--- Cadastrar Paciente ---")
    nome = input("Nome: ")
    cpf = input("CPF (11 dígitos): ")
    while not validar_cpf(cpf):
        print("CPF inválido. Tente novamente.")
        cpf = input("CPF (11 dígitos): ")

    idade = input("Idade: ")
    while not validar_idade(idade):
        print("Idade inválida. Deve ser um número.")
        idade = input("Idade: ")

    idade_num = int(idade)
    tipo = input("Tipo de reabilitação (motora, cognitiva, etc): ")
    paciente = [nome, cpf, idade_num, tipo]
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

# Função para listar pacientes
def listar_pacientes():
    print("\n--- Pacientes Cadastrados ---")
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
    else:
        i = 1
        for p in pacientes:
            print(str(i) + ". Nome: " + p[0] + " | CPF: " + p[1] + " | Idade: " + str(p[2]) + " | Reabilitação: " + p[3])
            i += 1

# Função para confirmar presença
def confirmar_presenca():
    print("\n--- Confirmar Presença ---")
    cpf = input("Informe seu CPF: ")
    if not validar_cpf(cpf):
        print("CPF inválido.")
    else:
        encontrado = False
        for p in pacientes:
            if p[1] == cpf:
                presencas.append(cpf)
                print("Presença confirmada para " + p[0])
                encontrado = True
        if not encontrado:
            print("Paciente não encontrado.")

# Função para cancelar consulta
def cancelar_consulta():
    print("\n--- Cancelar Consulta ---")
    cpf = input("Informe seu CPF: ")
    nova_lista = []
    cancelado = False
    for p in pacientes:
        if p[1] != cpf:
            nova_lista.append(p)
        else:
            cancelado = True
            print("Consulta de " + p[0] + " cancelada.")
    if not cancelado:
        print("Paciente não encontrado.")
    pacientes[:] = nova_lista

# Função com orientações pré-consulta
def mostrar_orientacoes():
    print("\n--- Orientações Pré-Consulta ---")
    print("1. Garanta uma boa conexão com a internet.")
    print("2. Escolha um local silencioso e bem iluminado.")
    print("3. Posicione a câmera na altura dos olhos.")
    print("4. Tenha seus documentos em mãos.")
    print("5. Clique no link da consulta com 10 minutos de antecedência.")

# Menu principal
def menu():
    sair = False
    while not sair:
        print("\n=== Assistente Virtual HC ===")
        print("1. Cadastrar Paciente")
        print("2. Visualizar Pacientes")
        print("3. Confirmar Presença")
        print("4. Cancelar Consulta")
        print("5. Orientações Pré-Consulta")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_paciente()
        elif escolha == '2':
            listar_pacientes()
        elif escolha == '3':
            confirmar_presenca()
        elif escolha == '4':
            cancelar_consulta()
        elif escolha == '5':
            mostrar_orientacoes()
        elif escolha == '6':
            print("Encerrando o seu atendimento. Obrigado!")
            sair = True
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
menu()