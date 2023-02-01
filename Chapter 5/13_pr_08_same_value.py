lang = {}
for i in range(1,5):
    name = input("enter your name: ")
    language = input("enter you favourite language: ")
    lang.update({name:language})
print(lang)
# only the keys should be different , values can stay common