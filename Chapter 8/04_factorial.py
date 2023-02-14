def factorial(n):
    product = 1
    for i in range (n):
        product = product * (i+1)
    return product

print(factorial(5))
# can also be assigned to a variable

fact = factorial(5)
print(fact,"Assigned to a variable")