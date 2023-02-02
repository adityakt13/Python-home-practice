sub1 = int(input("Enter the marks of subject no.1: "))
sub2 = int(input("Enter the marks of subject no.2: "))
sub3 = int(input("Enter the marks of subject no.3: "))

if sub1 <33 or sub2 <33 or sub3 <33:
    print("You failed because you scored less than 33% marks in one of the subject")
elif (sub1+sub2+sub3) /3 <40:
    print("You have failed because your overall percentage is less than 40% ")
else:
    print("You are promoted to the next class")