"""Crie um função que receba uma string e que conte e retorne o número de vogais desta string."""
def func(x):
    count = 0
    for j in x:
        if j == "A" or j == "E" or j == "I" or j == "O" or j == "U":
            count += 1
    return count

num = input("Digite a string: ")
result = func(num)
print(result)
