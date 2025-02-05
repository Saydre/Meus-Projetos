# Definindo os inputs e as variaveis
carrosVendidos = int(input("Numero de carros vendidos: "))
totalVendas = float(input("Digite o valor total das vendas: "))
salarioFixo = float(input("Digite o valor do salario fixo do funcionario: "))
comissaoCarros = float(input("Digite a comissao por carro: "))

# Ccomissao das vendas
comissaoVendas = 0.05 * totalVendas

# Comissao total
comissaoTotal = (comissaoCarros * carrosVendidos) + comissaoVendas

# Salario final
salarioFinal = salarioFixo + comissaoTotal

# Printa o salario final
print("O salario final do vendedor é: R$ {:.2f}".format(salarioFinal))