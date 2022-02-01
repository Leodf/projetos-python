from cmath import sqrt

def calcular_raio(x, y):
    raio = y**2 + y*3 + sqrt(x)+5
    return raio

raio = calcular_raio(5,7)
print(raio)
raio = calcular_raio(4,5)
print(raio)