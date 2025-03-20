# ao contrario das listas, as tuplas são imutáveis

ponto = (3, 4)

print(ponto[0])  # Imprime 3
print(ponto[1])  # Imprime 4


# métodos de tupla

minha_tupla = (1, 2, 3, 2, 4, 2)

print(minha_tupla.count(2))  # Retorna 3
print(minha_tupla.index(3))  # Retorna 2
print(minha_tupla.index(2))  # Retorna 1
print(minha_tupla.index(2, 2))  # Retorna 3 (a partir do índice 2)
print(minha_tupla.index(2, 2, 4))  # Retorna 3 (entre os índices 2 e 4)
print(len(minha_tupla))  # Retorna 6
print(minha_tupla[1:3])  # Retorna (2, 3)
print(minha_tupla[1:5:2])  # Retorna (2, 4)
