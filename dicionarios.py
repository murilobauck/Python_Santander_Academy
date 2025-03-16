pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa["nome"])  # Imprime "João"
print(pessoa["idade"])    # Imprime 25
print(pessoa["cidade"])  # Imprime "Madri"


# metodos de dicionario

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


print(pessoa.keys())    # Imprime keys(["nome", "idade", "cidade"])
print(pessoa.values())  # Imprime values(["João", 25, "Madri"])
print(pessoa.items())   # Imprime items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])


pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}