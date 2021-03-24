import Animate
def CheckPalindrome():
    done = False
    while done == False:
        usertext = input('Please give me a text:       ')
        usertext = usertext.replace(' ', '')
        usertext = usertext.lower()
        length = len(usertext) - 1
        newtext = ''
        for i in range(length, -1, -1):
            newtext += usertext[i]
        if usertext == newtext:
            Animate.animate('The two strings are palindromes')
        else:
            Animate.animate('The two strings are not palindromes')
        useryesorno = input('Would you like to try again? Type y or Y for yes and n or N for no:        ')
        if useryesorno == 'y' or useryesorno == 'Y':
            done = False
        elif useryesorno == 'n' or useryesorno == 'N':
            done = True
        else:
            Animate.animate('Invalid response entered. Will start again')
    return 'Done'

CheckPalindrome()