# ==============================
# Assistente Virtual HC - Sistema de Teleconsultas
# Estrutura: CRUD em listas de listas
# ==============================

# ------------------------------
# Funções de validação
# ------------------------------

def validar_cpf(cpf):
    """Valida se o CPF possui 11 dígitos numéricos"""
    return len(cpf) == 11 and cpf.isdigit()

def validar_idade(idade):
    """Valida se a idade é um número inteiro maior que zero"""
    return idade.isdigit() and int(idade) > 0

def validar_tipo(tipo):
    """Valida se o tipo de reabilitação é válido"""
    tipos_validos = ["motora", "cognitiva", "física", "ocupacional"]
    return tipo.lower() in tipos_validos

# ------------------------------
# Funções CRUD de Pacientes
# ------------------------------

def cadastrar_paciente(pacientes):
    """Cadastra um novo paciente, validando CPF, idade e tipo"""
    print("\n--- Cadastrar Paciente ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return pacientes

    cpf = input("CPF (11 dígitos): ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido. Tente novamente.")
        cpf = input("CPF (11 dígitos): ").strip()

    # Evita duplicidade de CPF
    for p in pacientes:
        if p[1] == cpf:
            print("CPF já cadastrado!")
            return pacientes

    idade = input("Idade: ").strip()
    while not validar_idade(idade):
        print("Idade inválida. Deve ser um número maior que zero.")
        idade = input("Idade: ").strip()

    try:
        idade_num = int(idade)
    except ValueError:
        print("Erro ao converter idade. Cadastro cancelado.")
        return pacientes

    tipo = input("Tipo de reabilitação (motora, cognitiva, física, ocupacional): ").strip()
    if not tipo or not validar_tipo(tipo):
        tipo = "Não informado"

    paciente = [nome, cpf, idade_num, tipo]
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")
    return pacientes

def listar_pacientes(pacientes):
    """Lista todos os pacientes cadastrados"""
    print("\n--- Pacientes Cadastrados ---")
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
    else:
        for i, p in enumerate(pacientes, start=1):
            print(f"{i}. Nome: {p[0]} | CPF: {p[1]} | Idade: {p[2]} | Reabilitação: {p[3]}")

def atualizar_paciente(pacientes):
    """Atualiza informações de um paciente existente"""
    print("\n--- Atualizar Paciente ---")
    cpf = input("Digite o CPF do paciente que deseja atualizar: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return pacientes

    for p in pacientes:
        if p[1] == cpf:
            novo_nome = input(f"Novo nome ({p[0]}): ").strip()
            if novo_nome:
                p[0] = novo_nome

            nova_idade = input(f"Nova idade ({p[2]}): ").strip()
            if nova_idade:
                if validar_idade(nova_idade):
                    try:
                        p[2] = int(nova_idade)
                    except ValueError:
                        print("Erro ao atualizar idade. Mantendo anterior.")
                else:
                    print("Idade inválida. Mantendo anterior.")

            novo_tipo = input(f"Novo tipo de reabilitação ({p[3]}): ").strip()
            if novo_tipo:
                if validar_tipo(novo_tipo):
                    p[3] = novo_tipo
                else:
                    print("Tipo inválido. Mantendo anterior.")

            print("Paciente atualizado com sucesso!")
            return pacientes
    print("Paciente não encontrado.")
    return pacientes

def excluir_paciente(pacientes, presencas):
    """Exclui um paciente do sistema"""
    print("\n--- Excluir Paciente ---")
    cpf = input("Digite o CPF do paciente a ser excluído: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return pacientes, presencas

    for i, p in enumerate(pacientes):
        if p[1] == cpf:
            confirmar = input(f"Tem certeza que deseja excluir {p[0]}? (s/n): ").lower()
            if confirmar != 's':
                print("Exclusão cancelada.")
                return pacientes, presencas

            pacientes.pop(i)
            if cpf in presencas:
                presencas.remove(cpf)
            print(f"Paciente {p[0]} excluído com sucesso!")
            return pacientes, presencas
    print("Paciente não encontrado.")
    return pacientes, presencas

# ------------------------------
# Funções de presença e cancelamento
# ------------------------------

def confirmar_presenca(pacientes, presencas):
    """Confirma a presença do paciente"""
    print("\n--- Confirmar Presença ---")
    cpf = input("Informe seu CPF: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return presencas
    for p in pacientes:
        if p[1] == cpf:
            if cpf in presencas:
                print("Presença já confirmada.")
            else:
                presencas.append(cpf)
                print(f"Presença confirmada para {p[0]}")
            return presencas
    print("Paciente não encontrado.")
    return presencas

def cancelar_consulta(pacientes, presencas):
    """Cancela a consulta de um paciente"""
    print("\n--- Cancelar Consulta ---")
    cpf = input("Informe seu CPF: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return pacientes, presencas

    if cpf in presencas:
        presencas.remove(cpf)

    for i, p in enumerate(pacientes):
        if p[1] == cpf:
            pacientes.pop(i)
            print(f"Consulta de {p[0]} cancelada.")
            return pacientes, presencas
    print("Paciente não encontrado.")
    return pacientes, presencas

# ------------------------------
# Função de orientações pré-consulta
# ------------------------------

def mostrar_orientacoes():
    """Exibe orientações antes da consulta"""
    print("\n--- Orientações Pré-Consulta ---")
    print("1. Garanta uma boa conexão com a internet.")
    print("2. Escolha um local silencioso e bem iluminado.")
    print("3. Posicione a câmera na altura dos olhos.")
    print("4. Tenha seus documentos em mãos.")
    print("5. Clique no link da consulta com 10 minutos de antecedência.")

# ------------------------------
# Submenus
# ------------------------------

def submenu_crud_pacientes(pacientes, presencas):
    while True:
        print("\n--- Menu de Pacientes (CRUD) ---")
        print("1. Cadastrar Paciente")
        print("2. Listar Pacientes")
        print("3. Atualizar Paciente")
        print("4. Excluir Paciente")
        print("5. Voltar")
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
            print("Opção inválida.")
    return pacientes, presencas

def submenu_presencas(pacientes, presencas):
    while True:
        print("\n--- Menu de Presenças ---")
        print("1. Confirmar Presença")
        print("2. Cancelar Consulta")
        print("3. Voltar")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            presencas = confirmar_presenca(pacientes, presencas)
        elif escolha == '2':
            pacientes, presencas = cancelar_consulta(pacientes, presencas)
        elif escolha == '3':
            break
        else:
            print("Opção inválida.")
    return pacientes, presencas

# ------------------------------
# Menu principal
# ------------------------------

def menu_principal():
    pacientes = []
    presencas = []
    sair = False
    while not sair:
        print("\n=== Assistente Virtual HC ===")
        print("1. Gerenciar Pacientes")
        print("2. Presenças e Cancelamentos")
        print("3. Orientações Pré-Consulta")
        print("4. Sair")
        escolha = input("Escolha uma opção: ").strip()

        try:
            if escolha == '1':
                pacientes, presencas = submenu_crud_pacientes(pacientes, presencas)
            elif escolha == '2':
                pacientes, presencas = submenu_presencas(pacientes, presencas)
            elif escolha == '3':
                mostrar_orientacoes()
            elif escolha == '4':
                print("Encerrando o atendimento. Obrigado!")
                sair = True
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# ------------------------------
# Início do programa
# ------------------------------

if __name__ == "__main__":
    menu_principal()
