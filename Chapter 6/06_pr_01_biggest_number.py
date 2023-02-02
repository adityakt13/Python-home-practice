num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))

if num1 >num2:
    f1 = num1
else :
    f1 = num2

if num3 > num4:
    f2 = num3
else :
    f2 = num4

if f1 > f2:
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")

# second way
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))

if num1 >num2 and num2 > num3 and num3> num4:
    f1 = num1 
elif num2 > num1 and num1> num3 and num3 > num4:
    f1 = num2
elif num3 > num1 and num1> num2 and num2> num4:
    f1 = num3
elif num4 > num1 and num1 > num2 and num2 > num3:
    f1 = num4
print(f1) # NameError: name 'f1' is not defined