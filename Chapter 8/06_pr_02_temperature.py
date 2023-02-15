def farh (cel):
    return (cel *1.8) +32

celcius = int(input("Enter temperature in celcius: "))
fahrenheit = farh(celcius)

print(f"The temperature in celcius is {celcius} and {fahrenheit} in fahrenheit")