inp1 = input("Enter a string: ")
dsp = inp1.count('  ')
if dsp >=1:
    print(f'{dsp} double spaces detected')
else:
    print("No double spaces detected")
ssp = inp1.replace("  "," ")
print("--"*20)
print(ssp)