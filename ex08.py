# Elabore um programa que receba do usuário um número com 3 algarismos (123, 435 ou 786, etc.)

# • Imprima esse número ao contrário (321, 534 ou 687, e assim por diante)
# • Contudo, você só pode usar operações aritméticas (+, -, *, /, %).

# Descreva como você faria e mostre esse código

# METODO 1
# numero_string = input("Insira um numero\n> ")
# string_nova = ""

# for letra in numero_string:
#     string_nova = letra + string_nova

# print(string_nova)

# METODO 2
numero = int(input("Insira um numero\n> "))
numero_reverso = 0

while numero > 0:
		# Pega a sobra da divisão, que sera o último digito
		ultimoDigito = numero % 10 
		
		# Multiplica o numero por 10 para que a soma com o ultimo digito o encaixe no final
		numero_reverso = (numero_reverso * 10) + ultimoDigito 
	
		# Remove o ultimo digito dividindo o numero por 10
		numero = numero // 10

print("> ", numero_reverso)