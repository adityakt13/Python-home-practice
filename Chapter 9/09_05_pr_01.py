f = open('poem.txt')
t = f.read()
if 'Twinkle' in t:
    print('Twinkle is there')
else:
    print('Twinkle is npot there')
f.close()