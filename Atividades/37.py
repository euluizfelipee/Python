"""Crie um programa que faça o calculo do fatorial de um número. O fatorial a ser calculado deve ser recebido por input."""
num = int(input("Digite o numero: "))
mult = 1
for i in range(num, 0, -1):
    mult *= i
print(mult) 
