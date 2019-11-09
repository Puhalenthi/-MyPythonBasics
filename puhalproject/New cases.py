a = input("Give me a paragraph")
b = 0
index = a[b]
sentences = 0
words = 0

for index in a:
    if (index == " "):
        words += 1
    elif (index == "."):
        sentences += 1
    else:
        continue
    b += 1

words += 1
words = str(words)
sentences = str(sentences)
print("There are " + words + " words")
print("There are " + sentences + " sentences")
