

def animate(string):
    string = string
    length = len(string)
    for x in range(length):
        print(string[x], end='', flush=True)
        time.sleep(0.1)
    print(' [hit enter to continue]', end='')
    input()

if __name__ == '__main__':
    animate('Hello')
    animate('Hello')
    animate('Hello')
    animate('Hello there guys my name is Puhal')