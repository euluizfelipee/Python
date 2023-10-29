"""Crie um programa que diga “se você precisar ir ao mercado”. Você precisa ir ao mercado se “faltar comida” ou “se for sábado”. 
Mostre na saída do programa o valor lógico, indicando sim ou não."""
faltar_comida = True
e_sabado = True

precisa_ir_ao_mercado = faltar_comida or e_sabado

if precisa_ir_ao_mercado:
    print("Você precisa ir ao mercado.")
else:
    print("Você não precisa ir ao mercado.")
