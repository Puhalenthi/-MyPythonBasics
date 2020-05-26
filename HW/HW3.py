num = int(input('Enter the number of rows:      '))     #The number of rows
for i in range(num, 0, -1):     #Making a for loop that goes backwards
    list1 = [' '] * ((num * 2) - 1)     #Creating a list of empty strings
    length = len(list1) - 1     #Finding the length of the list
    if i == num:        #Checking to see if we are running the loop for the first time
        x = 0       #Setting a variable to zero
        list1 = ['A'] * ((num * 2) - 1)     #If we are running the loop for the first time, every element should be a letter
    else:       #If we are not running the loop for the first time
        list1[x] = 'A'      #Setting the first 'A' in the list
        list1[length - x] = 'A'     #Setting the last 'A' in the list
    string = ''     #Assigning a variable to an empty string
    for char in list1:      #Looping through the list
        string += char      #Adding every element in the list into the string
    print(string)       #Printing the string
    x += 1      #Incrementing the variable and then going on to the next row.