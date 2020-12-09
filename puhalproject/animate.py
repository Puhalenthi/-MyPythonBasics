import time

def animate(string):
    string = string
    length = len(string)
    for x in range(length):
        print(string[x], end='', flush=True)
        time.sleep(0.01)
    print(' [hit enter to continue]', end='')
    input()

animate('Hello')
animate('Hello')
animate('Hello')
animate('Hello')