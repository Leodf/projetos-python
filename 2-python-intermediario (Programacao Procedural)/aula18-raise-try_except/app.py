
def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass # retorna None por padrão

while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is not None:
        print(numero * 5)
        break
    else:
        print('Isso não é um número.')