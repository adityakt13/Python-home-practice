age = int(input("enter your age: "))
if age <18 :
    print("You are still a minor.")
elif age >=18 and age <= 25:
    print("Study hard and find a job.")
elif age > 25 and age <=45:
    print("This is a perfect time to work.")
elif age >45 and age <57 :
    print("You should plan for your retirement.")
else:
    print("Happy retirement to you.")
a = "I love my India"
print(a[::-2])