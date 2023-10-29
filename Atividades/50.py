"""Percorra os números de 0 a 20 e crie um array, onde caso o número terminar com zero o valor devera ser '0', caso contrario devera ser '-'"""
array = []
for i in range(0, 21):
    if i % 10 == 0:
        array.append('0')
    else:
        array.append('-')
print(array)

