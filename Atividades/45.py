"""Crie uma lista contendo todos dias (número) do mês em que você nasceu. Em seguida receba por input o dia (número) em que você nasceu e remova desta lista. 
Ao final mostre o conteúdo da lista."""
dias_do_mes = list(range(1, 32))
print(dias_do_mes)
ano = int(input("Digite o dia: "))
dias_do_mes.remove(ano)
print(dias_do_mes)