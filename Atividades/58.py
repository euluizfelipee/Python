""" Crie uma função que recebe um número arbitrário de parâmetros. Em seguida diga qual o tipo de cada parâmetro."""
def fun(*args):
    for i in args:
        print(type(i))
fun(1,2,3,4,5,6,"ola","mundo",7.7)