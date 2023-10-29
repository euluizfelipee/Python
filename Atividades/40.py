"""Crie um programa que percorra os números de 3 até 30 e diga o número é primo ou não."""
for num in range(3, 31):
    is_prime = True
    
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    
    if is_prime:
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")
