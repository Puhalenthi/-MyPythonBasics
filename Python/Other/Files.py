alphabetdict = {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 0, 'k': 0,'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0, '.': 0, ',': 0, '\'': 0, '?': 0, '!': 0, '$': 0, '(': 0, ')': 0}
userfile = input('Give me the file location:        ')

try:
    with open(userfile, 'r') as f:
        text = f.read().lower()
        for i in text:
            if i in alphabetdict:
                alphabetdict[i] += 1
except:
    print('File not found')
    quit()


for k, v in alphabetdict.items():
    print(k, '->', v)
