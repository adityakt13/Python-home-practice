names = ["Aditya", "Xaid", "Udbhav","Avneesh","Amrit","Asit","Bharvi"]
name = input("Input a name: ")
if name.capitalize() in names:
    print("This name is in the names list")
else:
    print("This name is not in the names list")