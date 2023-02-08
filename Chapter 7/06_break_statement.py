for i in range(10):
    print(i)
    if i == 5:
        print("loop broken")
        break
else:
    print("Loop complete") # it won't get executed because loop broke before completion