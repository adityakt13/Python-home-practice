comment = input("Enter a text and try to avoid spam: ")
if ("make a lot of money", "buy now", "subscribe this", "click this" in comment):
    print("This comment contains a spam")
else:
    print("This comment doesn't contain a spam")