def remove_and_split (string,word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "   Aditya is a good boy  "
remove_and_split(this, "Aditya")
n = remove_and_split(this, "Aditya")
print(n)