# Interação na lista

# Instruções de repetição
lista = ['azul', 'verde', 'roxo']

# for
# for elemento in lista:
#   print("Elemento: " + elemento)
#   print("Terceira letra do elemento: " + elemento[2])
#   print("Elemento de posição 2 na lista: " + lista[1])

# while
i = 0
while i < len(lista):
    elemento = lista[i]
    if elemento == 'azul':
        print(elemento)
    elif elemento == 'verde':
        i += 1
        continue # interrompe o laço atual
    else:
        break # interrompe a repetição
    i += 1