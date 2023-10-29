"""rie um função que receba uma lista de elementos e um valor qualquer. Em seguida retorne um booleano dizendo se o valor foi encontrado ou 
não e também a posição onde foi encontrado."""
def encontra(array, item):
    for i in range(0,len(array)):
        if (array[i] == item):
            return True, i-1
    return False

arr = [1, '3', True, 'Olá', 7.1]
print(encontra(arr,"abc"))
print(encontra(arr,"Olá"))
print(encontra(arr,"True"))
print(encontra(arr,1))
print(encontra(arr,"0"))
print(encontra(arr,"8"))