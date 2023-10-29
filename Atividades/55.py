"""Crie um função que receba dois números e uma string dizendo se deve realizar a soma ou subtração do números."""
def operacao_numerica(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    else:
        return "Operação não reconhecida"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+ para soma, - para subtração): ")

resultado = operacao_numerica(num1, num2, operacao)
print("Resultado:", resultado)
