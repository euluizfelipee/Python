"""Crie um programa que receba como input uma string. Em seguida percorra a string e diga quantos espaços em branco essa string tem."""
str = input("Digite o s string: ")
count = 0
for i in str:
    if i == ' ':
        count += 1 
print(count)
