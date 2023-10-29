"""Crie um programa que diga se a senha esta correta e portanto você tem acesso ao sistema. A senha devera ser salva no código,
 e a tentativa deve ser lida por input."""
senha = int(input("Digite sua senha:"))
cofre = 1334
if senha == cofre:
    print("Acesso liberado")
else:
    print("Acesso Negado")
