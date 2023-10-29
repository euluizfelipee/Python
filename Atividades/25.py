"""Faça um programa que leia uma string através do input e diga se ela possui uma vogal."""
texto = str(input("Digite sua String:"))

if 'a' in texto or 'e' in texto or 'i' in texto or 'o' in texto or 'u' in texto:
    print("Possui vogal.")
else:
    print("Não possui vogal.")