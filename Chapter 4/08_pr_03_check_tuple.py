a1 = (1,3,5,7,4,7,9)
a1[0] = 5
print(a1)
#TypeError: 'tuple' object does not support item assignment

a2 = (1,3,5,7,4,7,9)
a2 = list(a2)
print(a2)