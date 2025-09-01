print("Bem vindo ao sistema de vendas da Gabriel Peluzio Corp")

valor_do_pedido = float(input("Qual o valor do pedido? R$ "))
qtd_de_parcelas = int(input("Em quantas parcelas deseja pagar? "))

if qtd_de_parcelas < 4:
    juros = 0
elif qtd_de_parcelas >= 4 and qtd_de_parcelas < 6:
    juros = 0.04
elif qtd_de_parcelas >= 6 and qtd_de_parcelas < 9:
    juros = 0.08
elif qtd_de_parcelas >= 9 and qtd_de_parcelas < 13:
    juros = 0.16
else:
    juros = 0.32

valor_da_parcela = (valor_do_pedido * (1 + juros)) / qtd_de_parcelas
valor_total_parcelado = valor_da_parcela * qtd_de_parcelas

print(f"O valor da parcela será de R$ {valor_da_parcela:.2f}")
print(f"O valor total do pedido parcelado será de R$ {valor_total_parcelado:.2f}")
print("Obrigado por comprar na Peluzio Corp!")