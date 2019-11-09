sentence = input("Give me a sentence")
restrictedList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 1, 2, 3, 4, 5, 6, 7, 8, 9, '$', '#']

for c in sentence:
    search = False

    for r in restrictedList:

        if c == r:
            search = True
            break

    if search == False:
        print(c)