Invitation = '''Dear name,
You played wonderfully, and hence you are selected to represent our team
BILL
Date- date'''
name = input("Enter whatever you want")
date = input("Enter a date")
Invitation = Invitation.replace ('name',name)
Invitation = Invitation.replace('date',date)
print(Invitation)