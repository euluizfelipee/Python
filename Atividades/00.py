primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

j = int(input("Digite um índice: "))
for i in range(len(primeirosNomes)):
    nome_completo = primeirosNomes[i] + ' ' + sobreNomes[i]
    idade = idades[i]
    print(f"{i} - {nome_completo} está com {idade} anos")
