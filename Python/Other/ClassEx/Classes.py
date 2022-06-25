'''import time
class Worker():
#       This is a worker class.\nThere are many methods such as change_name(), retire, etc.\nTo start, do Worker(name, age, profession, are_on_a_break).
    def __init__(self, name, age, profession, onbreak):
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__onbreak = onbreak
        time.sleep(1)
        self.__info
    def change_name(self, name):
        self.__name = name
        time.sleep(1)
        self.__info()
    def change_age_to(self, age):
        self.__age = age
        time.sleep(1)
        self.__info()
    def change_profession(self, profession):
        self.__profession = profession
        time.sleep(1)
        self.__info()
    def break_or_no_break(self, onbreak):
        self.__onbreak = onbreak
        time.sleep(1)
        self.__info()
    def retire(self):
        i = input('WARNING. If you type y, it will delete the attributes in the class. You will have to reassign them later.(y/n):        ')
        if i == 'y':
            print('Deleting profile', end='  ', flush=True)
            time.sleep(1)
            for _ in range(3):
                print('.', end='', flush=True)
                time.sleep(1)
                print('.', end='', flush=True)
                time.sleep(1)
                print('.', flush=True)
                time.sleep(1)
            print('Successfully deleted profile!!!')
            del self.__name, self.__age, self.__profession, self.__onbreak
    def __info(self):
        if self.__onbreak == True:
            print('{} is {} years old and works as a {}. He is on break right now.'.format(self.__name, self.__age, self.__profession))
        else:
            print('{} is {} years old and works as a {}. He is not break right now.'.format(self.__name, self.__age, self.__profession))
            time.sleep(1)


mike = Worker('Mike Wayner', 37, 'Construction Worker', False)'''
'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return 'My name is {} and I am {} years old.'.format(self.name, self.age)

a = Dog('dog', 5)
print(a)'''
'''
class A():
    v = 0
    def C(self):
        return 100

class B(A):
    v = 1
    def C(self):
        return 101

b = B()
print(b.v, b.C())'''
'''
with open('/Users/puhal/Documents/Python/GUI/Pygame/Tron.py', 'r') as f:
    contents = f.read()

sum = 0
spacesum = 0

for _ in contents:
    sum += 1
    if _ == " ":
        spacesum += 1

print(contents, sum, spacesum)'''

with open('/Users/puhal/documents/python/gui/pygame/Tron.py') as f:
    contents = f.read()

count = {}

for i in range(32, 127):
    count[chr(i)] = 0

for i in contents:
    count[i] += 1

for k, v in count.items():
    print('{} -> {}'.format(k, v))

