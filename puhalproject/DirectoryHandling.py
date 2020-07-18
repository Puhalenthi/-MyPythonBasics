import os

def DirectoryHandling(path, num):
    x = num
    indents = ' ' * x
    directories = os.listdir(path)
    for i in directories:
        a = path + '\\' + i
        if os.path.isdir(a) == True:
            print(indents, i, ':') 
            DirectoryHandling(path + '\\' + i, num  + 4)
        elif os.path.isfile(a) == True:
            print(indents, i)
        


        

DirectoryHandling(r'C:\\', 4)