# try/except/finally

try:
    # Código que pode gerar uma exceção
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é {resultado}")

except ValueError:
    print("Erro: Você deve digitar um número válido.")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

finally:
    print("Obrigado por utilizar o programa.")


# excecoes personalizadas

condicao = True


def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")


try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")
