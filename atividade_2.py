print('=' * 50)
print("Bem vindo a loja de marmitas da Gabriel Peluzio Corp")
print('=' * 50)
print("Cardápio:")
print("Sabores disponíveis: (BA) - Bife acebolado | (FG) - Frango grelhado ")
print("Tamanhos disponíveis: (P) - Pequena | (M) - Média | (G) - Grande")
print("Preços:")
print("Bife acebolado: P - R$ 20,00 | M - R$ 25,00 | G - R$ 30,00")
print("Frango grelhado: P - R$ 18,00 | M - R$ 23,00 | G - R$ 28,00")
print('=' * 50)
# EXIGÊNCIA 1: Mensagem de boas-vindas com nome e menu
total_pedido = 0.0
# EXIGÊNCIA 5: Acumulador para somar os valores dos pedidos
while True:
# EXIGÊNCIA 7: Estrutura while com break e continue
    while True:
        sabor = input("Digite o sabor da marmita (BA/FG) ou 'S' para sair: ").upper()
        if sabor == 'BA' or sabor == 'FG':
            break
        elif sabor == 'S':
            print("Obrigado por visitar a Gabriel Peluzio Corp!")
            exit()
        continue
     # EXIGÊNCIA 2: Input do sabor com validação
    while True:
        tamanho = input("Digite o tamanho da marmita (P/M/G) ou 'S' para sair: ").upper()
        if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
            break
        elif tamanho == 'S':
            print("Obrigado por visitar a Gabriel Peluzio Corp!")
            exit()
        continue
    # EXIGÊNCIA 3: Input do tamanho com validação
    if sabor == 'BA':
        if tamanho == 'P':
            total_pedido += 20.0
        elif tamanho == 'M':
            total_pedido += 25.0
        elif tamanho == 'G':
            total_pedido += 30.0
    elif sabor == 'FG':
        if tamanho == 'P':
            total_pedido += 18.0
        elif tamanho == 'M':
            total_pedido += 23.0
        elif tamanho == 'G':
            total_pedido += 28.0
    print(f"O total do pedido é R$ {total_pedido:.2f}")
    # EXIGÊNCIA 4: If/elif/else aninhados para calcular preço
    while True:
        continuar = input("Deseja fazer outro pedido? (S/N): ").upper()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print("Digite S para Sim ou N para Não")
            continue
    if continuar == 'N':
        break
    # EXIGÊNCIA 6: Perguntar se deseja pedir mais algo
    
print("\n" + "=" * 50)
print(f"TOTAL DO PEDIDO: R$ {total_pedido:.2f}")
print("Obrigado pela preferência! Volte sempre!")
print("=" * 50)
#EXIGÊNCIA 6: Exibir o total final do pedido
        
    

        

