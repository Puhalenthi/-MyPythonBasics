import time
class Worker():
    def __init__(self, name, age, profession, onbreak):
        self.name = name
        self.age = age
        self.profession = profession
        self.onbreak = onbreak
    def change_name(self, name):
        self.name = name
        print('Successfully changed name to {}'.format(self.name))
    def add_age(self, age):
        self.age = age
        print('Successfully changed name to {}'.format(self.age))
    def change_profession(self, profession):
        self.profession = profession
        print('Successfully change profession to {}'.format(self.profession))
    def have_a_break(self):
        if self.onbreak == True:
            print('You are already on a break silly!!!')
        else:
            print('Started break')
    def finish_the_break(self):
        if self.onbreak == False:
            print('Your not on a break silly !!!')
        else:
            print('Finished break')
    def retire(self):
        i = input('WARNING. If you type y, it will delete the attributes in the class. You will have to reassign them later.(y/n):        ')
        if i == 'y':
            print('Deleting profile', end='  ', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', flush=True)
            time.sleep(1)
            print('Successfully deleted profile!!!')
            del self.name, self.age, self.profession, self.onbreak
    def __str__(self):
        if self.onbreak == True:
            print('{} is {} years old and works as a {}. He is on break right now.'.format(self.name, self.age, self.profession))
        else:
            print('{} is {} years old and works as a {}. He is not break right now.'.format(self.name, self.age, self.profession))
    def info(self):
        if self.onbreak == True:
            print('{} is {} years old and works as a {}. He is on break right now.'.format(self.name, self.age, self.profession))
        else:
            print('{} is {} years old and works as a {}. He is not break right now.'.format(self.name, self.age, self.profession))


mike = Worker('Mike Wayner', 37, 'Construction Worker', False)

mike.retire()