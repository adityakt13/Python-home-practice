# creating adding values in a set
s = set()
s.add((2,78,9,45)) 
s.add(47)
s.add(79)
s.add(90)
s.add(100)
s.add(15)
print(s)
# s.add({4:6,7:8}) # can't add dictionary to set
# s.add([1,3,5,7]) # can't add list to set
# print(s)

# length of set
print(len(s))

# removing elements in set
s.remove(90)
print(s)
s.pop()
print(s)

set1 = {1,3,5,7,9,10,11}
set2 = {2,4,6,8,9,10,11}
setunion = set1.union(set2) # same as set2.union(set1)
print(setunion)
setintersect = set2.intersection(set1) # same as set1.intersection(set2)
print(setintersect)