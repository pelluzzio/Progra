print("="*60)
print("bem-vindo ao sistema de gerenciamento de funcionarios da Gabriel Peluzio Corp!")
print("="*60)
# EXIGÊNCIA 1: Mensagem de boas-vindas com nome e sobrenome

id_global = 5562081 
lista_funcionarios = []
# EXIGÊNCIA 2: Lista de funcionários e id_global com valor do RU

def cadastrar_funcionario(id_func):
    print(f"\n--- Cadastro de Funcionário (ID: {id_func}) ---")
    nome = input("Digite o nome do funcionário: ").strip()
    setor = input("Digite o setor do funcionário: ").strip()

    while True:
        try:
            salario = float(input("Digite o salário do funcionário: ").replace(',', '.'))
            if salario < 0:
                print("Salário inválido! Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número válido para o salário.")
# EXIGÊNCIA 3: Função para cadastrar funcionário

    funcionario = {
        'ID': id_func,
        'Nome': nome,
        'Setor': setor,
        'Salário': salario
    }
    # EXIGÊNCIA 7: Dicionário dentro da lista

    lista_funcionarios.append(funcionario)
    print(f"Funcionário {nome} cadastrado com sucesso!")
    return id_func + 1

def consultar_funcionario():
    while True:
        print("\n--- Consulta de Funcionário ---")
        print("1 - Consultar todos os funcionários")
        print("2 - Consultar por ID")
        print("3 - Consultar por Setor")
        print("4 - Voltar ao menu principal")
        
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                if not lista_funcionarios:
                    print("Nenhum funcionário cadastrado.")
                else:
                    for func in lista_funcionarios:
                        print(f"ID: {func['ID']}, Nome: {func['Nome']}, Setor: {func['Setor']}, Salário: R$ {func['Salário']:.2f}")
            elif opcao == 2:
                try:
                    id_consulta = int(input("Digite o ID do funcionário: "))
                    encontrado = False
                    for func in lista_funcionarios:
                        if func['ID'] == id_consulta:
                            print(f"ID: {func['ID']}, Nome: {func['Nome']}, Setor: {func['Setor']}, Salário: R$ {func['Salário']:.2f}")
                            encontrado = True
                            break
                    if not encontrado:
                        print("Funcionário não encontrado.")
                except ValueError:
                    print("Entrada inválida! Digite um número inteiro para o ID.")
            elif opcao == 3:
                setor_consulta = input("Digite o setor: ").strip()
                encontrados = [func for func in lista_funcionarios if func['Setor'].lower() == setor_consulta.lower()]
                if not encontrados:
                    print("Nenhum funcionário encontrado nesse setor.")
                else:
                    for func in encontrados:
                        print(f"ID: {func['ID']}, Nome: {func['Nome']}, Setor: {func['Setor']}, Salário: R$ {func['Salário']:.2f}")
            elif opcao == 4:
                return
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite (1-4).")
# EXIGÊNCIA 4: Função para consultar funcionário

def remover_funcionario():
    while True:
        print("\n--- Remoção de Funcionário ---")
        try:
            id_remover = int(input("Digite o ID do funcionário a ser removido (ou '0' para voltar): "))
            if id_remover == 0:
                return
            encontrado = False
            for func in lista_funcionarios:
                if func['ID'] == id_remover:
                    lista_funcionarios.remove(func)
                    print(f"Funcionário {func['Nome']} removido com sucesso!")
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro para o ID.")
# EXIGÊNCIA 5: Função para remover funcionário
if __name__ == "__main__":
    while True:
        print("\n--- Menu Principal ---")
        print("1 - Cadastrar Funcionário")
        print("2 - Consultar Funcionário")
        print("3 - Remover Funcionário")
        print("4 - Sair")
        
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                id_global = cadastrar_funcionario(id_global)
            elif escolha == 2:
                consultar_funcionario()
            elif escolha == 3:
                remover_funcionario()
            elif escolha == 4:
                print("Obrigado por usar o sistema da Gabriel Peluzio Corp!")
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite (1-4).")