# ==============================
# Assistente Virtual HC - Sistema de Teleconsultas (Refatorado - sem any)
# Estrutura: CRUD em listas de dicionários
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
    """Valida se a reabilitação é válida"""
    tipos_validos = ["motora", "cognitiva", "física", "ocupacional"]
    return tipo.lower() in tipos_validos

# ------------------------------
# Funções CRUD de Pacientes
# ------------------------------

def cadastrar_paciente(pacientes):
    """Cadastra um novo paciente"""
    print("\n--- Cadastrar Paciente ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return pacientes

    cpf = input("CPF (11 dígitos): ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido.")
        cpf = input("CPF (11 dígitos): ").strip()

    # Evita duplicidade de CPF sem usar any()
    cpf_existe = False
    for p in pacientes:
        if p['cpf'] == cpf:
            cpf_existe = True
            break

    if cpf_existe:
        print("CPF já cadastrado!")
        return pacientes

    idade = input("Idade: ").strip()
    while not validar_idade(idade):
        print("Idade inválida. Deve ser número maior que zero.")
        idade = input("Idade: ").strip()

    tipo = input("Tipo de reabilitação (motora, cognitiva, física, ocupacional): ").strip()
    if not tipo or not validar_tipo(tipo):
        tipo = "Não informado"

    paciente = {
        "nome": nome,
        "cpf": cpf,
        "idade": int(idade),
        "tipo": tipo
    }

    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")
    return pacientes

def listar_pacientes(pacientes):
    """Lista todos os pacientes cadastrados"""
    print("\n--- Pacientes Cadastrados ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for i, p in enumerate(pacientes, start=1):
            print(f"{i}. Nome: {p['nome']} | CPF: {p['cpf']} | Idade: {p['idade']} | Reabilitação: {p['tipo']}")

def atualizar_paciente(pacientes):
    """Atualiza informações de um paciente existente"""
    print("\n--- Atualizar Paciente ---")
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
                if validar_idade(nova_idade):
                    try:
                        p['idade'] = int(nova_idade)
                    except ValueError:
                        print("Erro ao atualizar idade. Mantendo anterior.")
                else:
                    print("Idade inválida. Mantendo anterior.")

            novo_tipo = input(f"Novo tipo de reabilitação ({p['tipo']}): ").strip()
            if novo_tipo and validar_tipo(novo_tipo):
                p['tipo'] = novo_tipo

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
        if p['cpf'] == cpf:
            confirmar = input(f"Tem certeza que deseja excluir {p['nome']}? (s/n): ").lower()
            if confirmar != 's':
                print("Exclusão cancelada.")
                return pacientes, presencas

            pacientes.pop(i)
            presencas = [c for c in presencas if c != cpf]  # Remove presença
            print(f"Paciente {p['nome']} excluído com sucesso!")
            return pacientes, presencas

    print("Paciente não encontrado.")
    return pacientes, presencas

# ------------------------------
# Funções de presença e cancelamento
# ------------------------------

def confirmar_presenca(pacientes, presencas):
    """Confirma presença de um paciente"""
    print("\n--- Confirmar Presença ---")
    cpf = input("Informe seu CPF: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return presencas

    # Verificar se o CPF existe sem usar any()
    cpf_encontrado = False
    for p in pacientes:
        if p['cpf'] == cpf:
            cpf_encontrado = True
            break

    if cpf_encontrado:
        if cpf in presencas:
            print("Presença já confirmada.")
        else:
            presencas.append(cpf)
            print("Presença confirmada!")
    else:
        print("Paciente não encontrado.")

    return presencas

def cancelar_consulta(pacientes, presencas):
    """Cancela a consulta de um paciente"""
    print("\n--- Cancelar Consulta ---")
    cpf = input("Informe seu CPF: ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return pacientes, presencas

    presencas = [c for c in presencas if c != cpf]
    for i, p in enumerate(pacientes):
        if p['cpf'] == cpf:
            pacientes.pop(i)
            print(f"Consulta de {p['nome']} cancelada.")
            return pacientes, presencas

    print("Paciente não encontrado.")
    return pacientes, presencas

# ------------------------------
# Orientações pré-consulta
# ------------------------------

def mostrar_orientacoes():
    print("\n--- Orientações Pré-Consulta ---")
    print("1. Garanta boa conexão com a internet.")
    print("2. Escolha local silencioso e bem iluminado.")
    print("3. Posicione a câmera na altura dos olhos.")
    print("4. Tenha documentos em mãos.")
    print("5. Clique no link da consulta 10 minutos antes.")

# ------------------------------
# Submenus
# ------------------------------

def submenu_crud_pacientes(pacientes, presencas):
    while True:
        print("\n--- Menu de Pacientes ---")
        print("1. Cadastrar Paciente")
        print("2. Listar Pacientes")
        print("3. Atualizar Paciente")
        print("4. Excluir Paciente")
        print("5. Voltar")
        escolha = input("Escolha: ").strip()

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
        escolha = input("Escolha: ").strip()

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
    while True:
        print("\n=== Assistente Virtual HC ===")
        print("1. Gerenciar Pacientes")
        print("2. Presenças e Cancelamentos")
        print("3. Orientações Pré-Consulta")
        print("4. Sair")
        escolha = input("Escolha: ").strip()

        try:
            if escolha == '1':
                pacientes, presencas = submenu_crud_pacientes(pacientes, presencas)
            elif escolha == '2':
                pacientes, presencas = submenu_presencas(pacientes, presencas)
            elif escolha == '3':
                mostrar_orientacoes()
            elif escolha == '4':
                print("Encerrando o atendimento. Obrigado!")
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            pass  # espaço reservado para log ou limpeza

# ------------------------------
# Início do programa
# ------------------------------

if __name__ == "__main__":
    menu_principal()
