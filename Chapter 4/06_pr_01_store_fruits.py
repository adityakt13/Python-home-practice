list2 = []
fruit = input("Enter your favourite fruits: ")
for f in fruit.split():
    list2.append(f)
print(list2)
print(list2[2])


# another way
list2 = []
for i in range (1,8):
    list2.append(input(f"enter fruit name {i}: "))
print(list2)
print(list2[2])
# ask sir - what is a vector and what is a pipe ?