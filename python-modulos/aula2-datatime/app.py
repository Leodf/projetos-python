# https://docs.python.org/3.0/library/datetime.html

from datetime import datetime, timedelta

# data = datetime(2022,3,28,12,35)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

"""
data = datetime.strptime('20/04/2020', '%d/%m/%Y')
print(data.timestamp())

data2 = datetime.fromtimestamp(1587351600.0)
print(data2)
"""
"""
data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(seconds=2*60*60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
"""
d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:00:00', '%d/%m/%Y %H:%M:%S')

diff = d2 - d1
print(diff)
print(diff.total_seconds())
print(diff.days)

