post = input(("Enter a post: "))
check = "Aditya"
if check.lower() in post or check in post :
    print("Found the 'check'")
else:
    print("Didn't found the check")