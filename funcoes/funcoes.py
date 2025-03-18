def saudacao():
    print("Olá, mundo!")

saudacao()  # Imprime "Olá, mundo!"


def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")  # Imprime "Olá, João!"
saudacao("Maria")  # Imprime "Olá, Maria!"


# valores de retorno

def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  # Imprime 7


# labda são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas

quadrado = lambda x: x ** 2
print(quadrado(5))  # Imprime 25


# funcoes globais e locais

def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20
print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.