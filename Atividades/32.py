"""Crie um programa que receba 5 números, realiza a soma destes números, mas caso um destes números seja negativo não considere ele na soma.""" 
chave = 0

for j in range(5):
    h = int(input("Digite um número: "))
    if h >= 0:
        chave += h
print(chave)