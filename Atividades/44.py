"""Crie uma lista contendo o nome de todos os meses do ano. Em seguida receba por input o mês (número) em
 que você nasceu e mostre qual o nome do mês que você nasceu."""
lista = ["Janeiro", "Fevereiro","Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
ano = int(input("Digite o mes: "))
print(lista[ano-1])