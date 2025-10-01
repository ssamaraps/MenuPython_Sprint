# ==============================
# Assistente Virtual HC - Sistema de Teleconsultas
# Integrantes: 
# - Samara Porto Souza
# - Maria Gabriela Landim Severo
# - Eduarda Weiss Ventura
# ==============================

# funções de validação
def validar_cpf(cpf):
    """Valida se o CPF possui 11 dígitos numéricos"""
    return len(cpf) == 11 and cpf.isdigit()

def validar_idade(idade):
    """Valida se a idade é um número inteiro maior que zero"""
    return idade.isdigit() and int(idade) > 0

def validar_tipo(tipo):
    """Valida se a reabilitação informada é válida"""
    tipos_validos = ["motora", "cognitiva", "física", "ocupacional"]
    return tipo.lower() in tipos_validos

# funções CRUD de pacientes
def cadastrar_paciente(pacientes):
    """Cadastra um novo paciente"""
    print("\n--- Cadastro de Paciente ---")
    nome = input("Digite o nome do paciente: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return pacientes

    cpf = input("Digite o CPF (11 dígitos): ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido, tente novamente.")
        cpf = input("Digite o CPF (11 dígitos): ").strip()

    # Evita duplicidade de CPF
    cpf_existe = False
    for p in pacientes:
        if p['cpf'] == cpf:
            cpf_existe = True
            break

    if cpf_existe:
        print("Este CPF já está cadastrado no sistema.")
        return pacientes

    idade = input("Digite a idade: ").strip()
    while not validar_idade(idade):
        print("Idade inválida. Digite apenas números maiores que zero.")
        idade = input("Digite a idade: ").strip()

    tipo = input("Digite o tipo de reabilitação (motora, cognitiva, física, ocupacional): ").strip()
    if not tipo or not validar_tipo(tipo):
        tipo = "Não informado"

    try:
        paciente = {
            "nome": nome,
            "cpf": cpf,
            "idade": int(idade),
            "tipo": tipo
        }
        pacientes.append(paciente)
        print(f"Paciente {nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar o paciente: {e}")
    return pacientes

def listar_pacientes(pacientes):
    """Lista todos os pacientes cadastrados"""
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print("Nenhum paciente cadastrado até o momento.")
    else:
        for i, p in enumerate(pacientes, start=1):
            print(f"{i}. Nome: {p['nome']} | CPF: {p['cpf']} | Idade: {p['idade']} anos | Reabilitação: {p['tipo']}")

def atualizar_paciente(pacientes):
    """Atualiza informações de um paciente existente"""
    print("\n--- Atualização de Paciente ---")
    cpf = input("Digite o CPF do paciente que deseja atualizar: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return pacientes

    for p in pacientes:
        if p['cpf'] == cpf:
            novo_nome = input(f"Novo nome ({p['nome']}): ").strip()
            if novo_nome:
                p['nome'] = novo_nome

            nova_idade = input(f"Nova idade ({p['idade']}): ").strip()
            if nova_idade:
                try:
                    if validar_idade(nova_idade):
                        p['idade'] = int(nova_idade)
                    else:
                        print("Idade inválida. Mantendo a anterior.")
                except ValueError:
                    print("Erro ao atualizar idade. Mantendo a anterior.")

            novo_tipo = input(f"Novo tipo de reabilitação ({p['tipo']}): ").strip()
            if novo_tipo:
                if validar_tipo(novo_tipo):
                    p['tipo'] = novo_tipo
                else:
                    print("Tipo de reabilitação inválido. Mantendo o anterior.")

            print("Paciente atualizado com sucesso!")
            return pacientes

    print("Paciente não encontrado.")
    return pacientes

def excluir_paciente(pacientes, presencas):
    """Exclui um paciente do sistema"""
    print("\n--- Exclusão de Paciente ---")
    cpf = input("Digite o CPF do paciente a ser excluído: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return pacientes, presencas

    for i, p in enumerate(pacientes):
        if p['cpf'] == cpf:
            confirmar = input(f"Tem certeza que deseja excluir {p['nome']}? (s/n): ").lower()
            if confirmar != 's':
                print("Exclusão cancelada.")
                return pacientes, presencas
            try:
                pacientes.pop(i)
                presencas = [c for c in presencas if c != cpf]
                print(f"Paciente {p['nome']} foi excluído com sucesso!")
            except Exception as e:
                print(f"Erro ao excluir paciente: {e}")
            return pacientes, presencas

    print("Paciente não encontrado.")
    return pacientes, presencas

# funções de presença e cancelamento
def confirmar_presenca(pacientes, presencas):
    """Confirma presença de um paciente"""
    print("\n--- Confirmação de Presença ---")
    cpf = input("Digite seu CPF: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return presencas

    cpf_encontrado = False
    for p in pacientes:
        if p['cpf'] == cpf:
            cpf_encontrado = True
            break

    if cpf_encontrado:
        if cpf in presencas:
            print("Sua presença já foi confirmada anteriormente.")
        else:
            presencas.append(cpf)
            print("Presença confirmada com sucesso!")
    else:
        print("Paciente não encontrado.")
    return presencas

def cancelar_consulta(pacientes, presencas):
    """Cancela a consulta de um paciente"""
    print("\n--- Cancelamento de Consulta ---")
    cpf = input("Digite seu CPF: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return pacientes, presencas

    presencas = [c for c in presencas if c != cpf]
    for i, p in enumerate(pacientes):
        if p['cpf'] == cpf:
            try:
                pacientes.pop(i)
                print(f"Consulta de {p['nome']} cancelada com sucesso.")
            except Exception as e:
                print(f"Erro ao cancelar consulta: {e}")
            return pacientes, presencas

    print("Paciente não encontrado.")
    return pacientes, presencas

# orientações pré-consulta
def mostrar_orientacoes():
    print("\n--- Orientações Pré-Consulta ---")
    print("1. Garanta boa conexão com a internet.")
    print("2. Escolha um local silencioso e bem iluminado.")
    print("3. Posicione a câmera na altura dos olhos.")
    print("4. Tenha seus documentos em mãos.")
    print("5. Acesse o link da consulta 10 minutos antes do horário.")

# submenus
def submenu_crud_pacientes(pacientes, presencas):
    while True:
        print("\n--- Menu de Pacientes ---")
        print("1. Cadastrar Paciente")
        print("2. Listar Pacientes")
        print("3. Atualizar Paciente")
        print("4. Excluir Paciente")
        print("5. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            pacientes = cadastrar_paciente(pacientes)
        elif escolha == '2':
            listar_pacientes(pacientes)
        elif escolha == '3':
            pacientes = atualizar_paciente(pacientes)
        elif escolha == '4':
            pacientes, presencas = excluir_paciente(pacientes, presencas)
        elif escolha == '5':
            break
        else:
            print("Opção inválida, tente novamente.")
    return pacientes, presencas

def submenu_presencas(pacientes, presencas):
    while True:
        print("\n--- Menu de Presenças ---")
        print("1. Confirmar Presença")
        print("2. Cancelar Consulta")
        print("3. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            presencas = confirmar_presenca(pacientes, presencas)
        elif escolha == '2':
            pacientes, presencas = cancelar_consulta(pacientes, presencas)
        elif escolha == '3':
            break
        else:
            print("Opção inválida, tente novamente.")
    return pacientes, presencas

# menu principal
def menu_principal():
    pacientes = []
    presencas = []
    while True:
        print("\n=== Assistente Virtual HC ===")
        print("1. Gerenciar Pacientes")
        print("2. Presenças e Cancelamentos")
        print("3. Orientações Pré-Consulta")
        print("4. Sair do Sistema")
        escolha = input("Escolha uma opção: ").strip()

        try:
            if escolha == '1':
                pacientes, presencas = submenu_crud_pacientes(pacientes, presencas)
            elif escolha == '2':
                pacientes, presencas = submenu_presencas(pacientes, presencas)
            elif escolha == '3':
                mostrar_orientacoes()
            elif escolha == '4':
                print("Encerrando o atendimento. Obrigado por utilizar nosso sistema!")
                break
            else:
                print("Opção inválida, tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
        finally:
            print("Operação finalizada.")

# início do programa
if __name__ == "__main__":
    menu_principal()
