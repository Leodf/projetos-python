from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)