class IncorrectItemEnteredError(BaseException):
    pass
def BubbleSort():
    nums = []
    done = False
    sorting = True
    while done == False:
        try:
            num = int(input('Give me a number to add to the sorting list:      '))
        except:
            print('Please enter a valid integer')
        else:
            nums.append(num)
        finally:
            useryesorno = input('Would you like to add another number? Type y or Y for yes and n or N for no:       ')
            if useryesorno == 'y' or useryesorno == 'Y':
                done = False
            elif useryesorno == 'n' or useryesorno == 'N':
                done = True
            else:
                done = True
                raise IncorrectItemEnteredError('An Invalid Response Was Entered')
    length = len(nums)
    while sorting == True:
        newnums = nums.copy()
        for i in range(1, len(nums)):
            if newnums[i] < newnums[i - 1]:
                newnums[i], newnums[i - 1] = newnums[i - 1], newnums[i]
        
        print(newnums, '\n')
        if newnums == nums:
            sorting = False
        else:
            nums = newnums
    return 'Done'

print(BubbleSort())
