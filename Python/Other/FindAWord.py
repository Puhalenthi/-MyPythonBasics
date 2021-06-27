def FindAWord():
    usertext = input("Enter a word or sentence:     ")
    userword = input("Enter a word:     ")
    usertext = usertext.lower()
    userword = userword.lower()
    found = True
    start = 0
    for i in userword:
        pos = usertext.find(i, start) 
        if pos == -1:
            found = False
            break
        start = pos + 1
    if found == True:
        print("The word is in the text")
    else:
        print("The word is not in the text")
    return 'Done'


FindAWord()