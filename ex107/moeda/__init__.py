def metade(num = 0):
    met = num / 2
    return met

def dobro(num = 0):
    dob = num * 2
    return dob

def aumentar(num = 0, x = 0):
    a = num * (1 + (x / 100))
    return a  

def diminuir(num = 0, x = 0):
    a = num * (1 - (x / 100))
    return a

def moeda(x, moeda = 'R$'):
    return f'{moeda}{x:.2f}'.replace('.', ',')