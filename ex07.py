# EXERCÍCIO 7. Desenvolva um programa que utilize diversos tipos de dados

nome = "Joao"
idade = 22
cartao_fidelidade = False
lista_de_compras = [
	"Leite",
	"Pão",
	"Aveia"
]

print("====== Informações ======")
print(f"Cliente: {nome}, {idade} anos")

if idade >= 18:
	print("Maior de Idade")
else:
	print("Menor de Idade")

for item in lista_de_compras:
	if item == "Leite":
		print("Válido para a promoção do leite")

if cartao_fidelidade:
	print("Possui cartão fidelidade")
else:
	print("Não possui cartão fidelidade")