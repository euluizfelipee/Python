"""Crie um programa que responda se você foi aprovado numa prova. Você somente foi aprovado numa prova se sua média for maior 
ou igual que 7 ou se sua nota no exame for maior ou igual a 5. Leia esses valores por input."""
exame = int(input("Digite a nota no exame:"))
media = int(input("Digite sua media:"))
if media >= 7 or exame >= 5:
    print("Aprovado")
else:
    print("Reprovado")