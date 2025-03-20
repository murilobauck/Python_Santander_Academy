arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()


with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# o arquivo é aberto utilizando a declaração with e é fechado automaticamente uma vez que se sai do bloco with
