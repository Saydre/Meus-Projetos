# Definindo os inputs e as variaveis
morango_peso = float(input("Digite o peso total dos morangos em Kg: "))
maca_peso = float(input("Digite o peso total das maçãs em Kg: "))

# Calculando o custo dos morangos
if morango_peso <= 5:
    morango_custo = morango_peso * 2.5
else:
    morango_custo = morango_peso * 2.2

# Calculando o custo das maçãs
if maca_peso <= 5:
    maca_custo = maca_peso * 1.8
else:
    maca_custo = maca_peso * 1.5

# Calculando os custos
total_custo = morango_custo + maca_custo

# Checagem se haverá desconto e aplicando os 10% de disconto
if morango_peso + maca_peso > 8 or total_custo > 25:
    total_custo -= total_custo * 0.10

# Retorna o valor total dos cusstos
print("O custo total é: R$ {:.2f}".format(total_custo))