# f = open('another.txt', 'w')
# f.write("Please write this to the file")
# f.close()

f = open('another.txt', 'a')
f.write(" Here I am appending")
f.close()                              # if we run this multiple times , then it wil keep on appending