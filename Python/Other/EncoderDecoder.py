from Animate import animate
def EncoderDecoder():
    done = False
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while done == False:
        newtext = ''
        userencodeordecode = input('Would you like to encode or decode? Type e or E for encode and d or D for decode:        ')
        usertext = input('Please give me some text. Numbers are allowed:        ')
        usertext = usertext.lower()
        if userencodeordecode == 'e' or userencodeordecode == 'E':
            try:
                numshift = int(input('Enter the number to shift to the right by:        '))
                for i in usertext:
                    if i in letters:
                        currentindex = letters.index(i)
                        currentindex += numshift
                        indexdone = False
                        while indexdone == False:
                            if currentindex >= 26:
                                currentindex -= 26
                            else:
                                indexdone = True
                        newletter = letters[currentindex]
                        newtext += newletter
                    else:
                        newtext += i
                animate(newtext)
            except:
                animate('Invalid text entered. Try again')
        elif userencodeordecode == 'd' or userencodeordecode == 'D':
            try:
                numshift = int(input('Enter the number to shift to the left by:        '))
                for i in usertext:
                    if i in letters:
                        currentindex = letters.index(i)
                        currentindex -= numshift
                        indexdone = False
                        while indexdone == False:
                            if currentindex <= -1:
                                currentindex += 26
                            else:
                                indexdone = True
                        newletter = letters[currentindex]
                        newtext += newletter
                    else:
                        newtext += i
                animate(newtext)
            except:
                animate('Invalid text entered. Try again')
        else:
            animate('Invalid text entered:       {}. Please try again'.format(userencodeordecode))
        useryesorno = input('Would you like to try again? Type y or Y for yes and n or N for no:        ')
        if useryesorno == 'y' or useryesorno == 'Y':
            done = False
        elif useryesorno == 'n' or useryesorno == 'N':
            done = True
        else:
            animate('Invalid response entered. Will start again')
    return 'Finished EncoderDecoder... Click [ENTER] to leave'


animate(EncoderDecoder())