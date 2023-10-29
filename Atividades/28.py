"""Crie um programa que possui uma variável que guarde seu CPF e que guarde uma senha de sua escolha. Em seguida receba por input uma senha do usuário. 
Caso a senha recebida seja a correta mostre o CPF, caso não diga que a senha esta incorreta."""
senha = int(input("Digite sua senha: "))
correta = 1315
cpf = '123.456.789-00'

if senha == correta:
    print(cpf)
else:
    print("senha esta incorreta")