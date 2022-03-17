
novo_cnpj = '04252011000110'

novo_cnpj = novo_cnpj[:-2]

soma = 0
reverso = 0
lista_param = [5,4,3,2,9,8,7,6,5,4,3,2,6,5,4,3,2,9,8,7,6,5,4,3,2]
for indice, valor in enumerate(lista_param):
 
    if indice == 12 or indice == 24:
        digito = 11 - (soma % 11)

    soma += valor * int(novo_cnpj[indice])

    if indice > 11:
        indice -= 12 

        if digito > 9:
            digito = 0      
            
        soma = 0
        novo_cnpj += str(digito)
    
    
    
        

    
    

print(novo_cnpj)