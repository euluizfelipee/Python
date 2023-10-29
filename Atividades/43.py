"""Crie dois sets com os seguintes valores 30,4,43,52,65,-10 e 43,2,4,76,32,65,3. Agora faça a junção desses Sets, mas se houverem valores 
        repetidos entre ambos eles não podem repetir na lista unida."""
set1 = {30,4,43,52,65,-10}
set2 = {43,2,4,76,32,65,3}
unidos = set1.union(set2)
print(unidos)