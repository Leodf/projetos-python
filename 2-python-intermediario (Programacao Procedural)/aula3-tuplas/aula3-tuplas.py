
t1 = (1,2,3,'a', 'Leonardo')
t2 = 6,7,8,9,10
t3 = t1 + t2

n1, n2, n3, *_, n10= t3

print(t1)
print(t2)
print(t3)
print(n2)
print(n10)

t5 = (1,2,3,'Leo', 'Faveri') * 20

print(t5)

t6 = ('Leo', 'de', 'Faveri', 4)
print(t6)
t6 = list(t6)
t6[1] = 3000
t6 = tuple(t6)
print(t6)


