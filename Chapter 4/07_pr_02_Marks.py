mark_list = []
marks = input("Enter marks of seven students: ")
for m in marks.split():
    mark_list.append(m)
    mark_list.sort()
print(mark_list)
# ask sir how the values can be changed in to integer from string

mark_list = []
for m in range (1,7):
    mark_list.append(int(input(f"Enter marks of {m}st student: ")))
    mark_list.sort()
print(mark_list)