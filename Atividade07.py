# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.

prod = float(input("Valor do produto"))

FinalProd = float((prod * 0.12) + prod)

print(F"O valor é {FinalProd}")
