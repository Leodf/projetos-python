"""
CPF = 079.004.419-64
----------------------
 0 * 10 = 0             #   0 * 11 = 0
 7 * 9 = 63             #   7 * 10 = 70
 9 * 8 = 72             #   9 * 9 = 81
 0 * 7 = 0              #   0 * 8 = 0 
 0 * 6 = 0              #   0 * 7 = 0  
 4 * 5 = 20             #   4 * 6 = 24 
 4 * 4 = 16             #   4 * 5 = 20
 1 * 3 = 3              #   1 * 4 = 4 
 9 * 2 = 18             #   9 * 3 = 27
                        #   digito 1 * 2 = 12
soma = 192              #   soma = 238
11 - (192 % 11) = 6     #   11 - (238 % 11) = 4
se soma > 9 == 0        #   se soma > 9 == 0
se soma <= 9 == soma    #   se soma <= 9 == soma
Digito 1 = 6            #   Digito 1 = 4

"""
# Input de dados e verificação dos numeros
print()
print('*'*50)
titulo = ' Validador de CPF '
print(f'{titulo:*^50}')
print('*'*50)
print()

while True:
    cpf = input('Digite o seu CPF: ')
    if not cpf.isnumeric():
        print('Digite apenas os números do seu CPF sem ponto e hífen')
        continue 
    elif not len(cpf) == 11:
        print('Opa seu CPF está não está com 11 números')
        continue
    else:
        print(cpf)
        break

soma_1 = 0
i = 0
for n in range(10,1,-1):
    soma_1 += int(cpf[i])*n
    i += 1
calc_digito_1 = str (11 - (soma_1 % 11))

soma_2 = 0
j = 0
for n in range(11,1,-1):
    soma_2 += int(cpf[j])*n
    j += 1
calc_digito_2 = str (11 - (soma_2 % 11))

if calc_digito_1 == cpf[9] and calc_digito_2 == cpf[10]:
    print('Seu CPF é válido no território nacional')
else:
    print('Você está com um CPF não válido')




    

    






