"""Crie um programa que mostre o dia, mês, ano, hora, minuto e segundos inseridos pelo usuário. Formate o valor."""
dia = int(input("Digite o dia:"))
mes =int(input("Digite o mes:"))
ano = int(input("Digite o ano:"))
hora = int(input("Digite a hora:"))
minuto = int(input("Digite os minutos:"))
segundos = int(input("Digite os segundos:"))
data_formatada = "%d/%d/%d" % (dia, mes, ano)
hora_formatada = "%d:%d:%d" % (hora, minuto, segundos)
print(data_formatada)
print(hora_formatada)


