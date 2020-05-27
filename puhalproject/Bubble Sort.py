def sort():     #Creating a function
    done = False        #Creating a variable to see if we are done
    var = 0     #Making a variable
    while done == False:        #Checking to see if we are done with the while loop
        if var == 0:        #Checking to see if we are running the loop for the first time
            nums = []       #If we are, then we are making an empty list
        try:        #Just in case if our program has any errors
            usernum = input('Enter a random number so the computer can sort all of the numbers that you entered so far. Hit [ENTER] for the computer to start sorting!!!:       ')      #Asking the user for an input
            if usernum == '':       #If the user enters nothing
                done = True     #Setting the variable to True
            else:       #If the user enters some text
                usernum = int(usernum)      #Turning it into an int and if it is not a number, it will go to line 14
                nums.append(usernum)        #Adding the input into the list
        except:     #If something goes wrong in line 12
            print('You entered an invalid character try again')     #It will print a user friendly error
            return      #Exit the function
        var += 1        #Incrementing the variable
    userinput = input('Do you want it in increasing or decreasing order?:       ')      #Asking the user for increasing or decreasing order
    done = False        #Creating a variable to see if we are done
    length = len(nums) - 1      #Finding the length of the list of numbers
    var = 0     #Setting a variable to see if we are running the loop for the first time
    while done == False:        #Checking to see if we are done
        if userinput == 'increasing':       #Checking if it is increasing order
            for i in range(0, length):      #Making a for loop
                try:        #Just in case something goes wrong
                    if nums[i] > nums[i + 1]:       #Checking if the index is greater than
                        x = nums[i]     #Assigning a variable
                        nums[i] = nums[i + 1]       #Saving a copy of the variable
                        nums[i + 1] = x     #Assigning the previous variable
                        print(nums)     #Printing it to show how the program works
                except:     #If something goes wrong
                    pass        #It will do nothing
        elif userinput == 'decreasing':       #Checking if it is increasing order
            for i in range(0, length):      #Making a for loop
                try:        #Just in case something goes wrong
                    if nums[i] < nums[i + 1]:       #Checking if the index is less than
                        x = nums[i]     #Assigning a variable
                        nums[i] = nums[i + 1]       #Saving a copy of the variable
                        nums[i + 1] = x     #Assigning the previous variable
                        print(nums)     #Printing it to show how the program works
                except:     #If something goes wrong
                    pass        #It will do nothing
        else:       #If the user enters something else
            print('You entered an invalid value')
        if var == 0:        #If we are runnign the program for the first time
            prevnums = []       #Assigning a variable to an empty list
        if prevnums == nums:        #If the previous list of nums is the same as the current list of nums
            done = True     #We are changing the value of the variable to say that we are done with the sorting
            break       #Breaking out of the loop
        for index in nums:      #For every element in nums
            prevnums.append(index)      #We are appending them to prevnums 
        var += 1        #Incrementing the variable

sort()      #Calling the function in line 1