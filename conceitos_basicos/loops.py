# for

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)


# while

contador = 0

while contador < 5:

    print(contador)
    contador += 1

    if contador == 5:
        break  # break é utilizado para sair prematuramente de um loop


# continue

for i in range(10):

    if i % 2 == 0:
        continue  # continue é utilizado para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração.
    print(i)


# pass

for i in range(5):
    pass  # pass é uma operação nula que não faz nada.
    # pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.
