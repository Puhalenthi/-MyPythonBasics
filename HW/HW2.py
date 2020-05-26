num = int(input('Give me the number of rows:        '))     #Getting the number of rows
for i in range(num, num * 2 - 1):       #Creating a for loop to print each of the rows
    currentline = [' '] * i         #Making a list to store the spaces and 'A'
    length = len(currentline) - 1       #Finding the length of the list 
    currentline[length] = 'A'       #Setting the last element to an A
    if i > num:         #Checking to see if we already ran this code
        currentline[length - (2 * x)] = 'A'         #Setting the other part of the row to an A if the if statement is true
    else:       #If it is the first time we are running the loop
        x = 0       #Setting a variable to 0
    finalline = ''      #Creating an empty string
    for letter in currentline:      #Getting all the elements in the list
        finalline += letter         #Each element is being added one by one to the empty string
    print(finalline)        #Printing the string
    x += 1      #Incrementing x then go back to line 2

print('A' * ((num * 2) - 1))        #When the for loop is done, this will print the base.