mark = int (input("Enter your score: "))
if mark in range (91,100):
    print("Excellent")
elif mark in range(81,90):
    print("A")
elif mark in range (71,80):
    print("B")
elif mark in range (61,70):
    print("C")
elif mark in range (51,60):
    print("D")
else:
    print("F")