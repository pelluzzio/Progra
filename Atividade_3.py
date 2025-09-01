print("bem-vindo à fabrica de camisas da Gabriel Peluzio Corp!")
# EXIGÊNCIA 1: Mensagem de boas-vindas com nome e sobrenome
def escolha_modelo():
    while True:
        modelo = input("\nEscolha o modelo desejado(MCS/MLS/MCE/MLE) ou 'S' para sair: ").upper().strip()
        if modelo == 'MCS':
            print("Modelo selecionado: Manga Curta Simples - R$ 1,80")
            return 1.80
        elif modelo == 'MLS':
            print("Modelo selecionado: Manga Longa Simples - R$ 2,10")
            return 2.10
        elif modelo == 'MCE':
            print("Modelo selecionado: Manga Curta Estampada - R$ 2,90")
            return 2.90
        elif modelo == 'MLE':
            print("Modelo selecionado: Manga Longa Estampada - R$ 3,20")
            return 3.20
        elif modelo == 'S':
            print("Obrigado por visitar a Gabriel Peluzio Corp!")
            exit()
        else:
            print("Modelo inválido! Tente novamente.")
 # EXIGÊNCIA 2: Função para escolha do modelo
def escolha_quantidade():
    while True:
        try:
            quantidade = int(input("Digite a quantidade desejada ou '0' para sair: "))
            if  quantidade <0:
                print ("Quantidade inválida! Tente novamente.")
                continue
            elif quantidade == 0:
                print("Obrigado por visitar a Gabriel Peluzio Corp!")
                exit()
            elif quantidade >20000:
                print("Quantidade máxima excedida! Tente novamente.")
                continue
            
            if quantidade < 20:
                desconto = 0
            elif quantidade >= 20 and quantidade < 200:
                desconto = 0.05
            elif quantidade >= 200 and quantidade < 2000:
                desconto = 0.07
            elif quantidade >= 2000 and quantidade <=20000:
                desconto = 0.12
            
            valor_com_desconto = quantidade * (1 - desconto)
            return valor_com_desconto 
        
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

# EXIGÊNCIA 3: Função para número de camisetas com desconto        
def frete():
    while True:
        try:
            print("\nOpções de frete:")
            print("0 - Retirar na Fabrica (Grátis)")
            print("1 - transportadora (R$ 100,00)")
            print("2 - Sedex (R$ 200,00)")
            opcao = int(input("Escolha a opção de frete (0/1/2) ou '3' para sair: "))
            if opcao == 0:
                return 0.0, "Retirar na Fabrica"
            elif opcao == 1:
                return 100.0, "Transportadora"
            elif opcao == 2:
                return 200.0, "Sedex"
            elif opcao == 3:
                print("Obrigado por visitar a Gabriel Peluzio Corp!")
                exit()
            else:
                print("Opção inválida! Tente novamente.")
# EXIGÊNCIA 4: Função para escolha do frete
        except ValueError:
            print("Entrada inválida! Digite números.")
          # EXIGÊNCIA 6: Tratamento de erro para valores não numéricos
if __name__ == "__main__":
    valor_unitario = escolha_modelo()
    valor_camiseta = escolha_quantidade()
    valor_frete, tipo_frete = frete()
    
    total = (valor_unitario * valor_camiseta) + valor_frete
 # EXIGÊNCIA 5: Cálculo do total a pagar no código principal

    print("\n" + "=" * 50)
    print("Resumo do Pedido:")
    print(f"Valor Unitário da Camisa: R$ {valor_unitario:.2f}")
    print(f"Valor Total das Camisas (com desconto se aplicável): R$ {valor_camiseta * valor_unitario:.2f}")
    print(f"Valor do Frete ({tipo_frete}): R$ {valor_frete:.2f}")
    print(f"TOTAL DO PEDIDO: R$ {total:.2f}")
    print("Obrigado pela preferência! Volte sempre!")
    print("=" * 50)
