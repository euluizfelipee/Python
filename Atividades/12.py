"""Você tem um determinado números de ovos de páscoa para dividir entre um determinado número de pessoas (duas variáveis niciais). 
Determine quantos ovos ficarão por pessoa e quantos ovos sobrarão pois não puderam ser divido igualmente. Lembre o número de ovos por 
pessoa é um número inteiro."""

ovos = 37
pessoas = 6
ovos_por_pessoa = ovos // pessoas 
sobra = ovos % pessoas
print(f"Cada pessoa receberá {ovos_por_pessoa} ovos.")
print(f"Sobrarão {sobra} ovos.")