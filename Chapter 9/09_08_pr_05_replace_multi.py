words = ['donkey','horse','zebra','mule']
with open ("sample.txt") as f:
    content = f.read() 

for word in words:
    content = content.replace(word, "o(^.^)o")

with open("sample.txt", "w") as f:
    f.write(content)