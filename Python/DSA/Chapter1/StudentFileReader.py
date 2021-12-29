class Student:
    def __init__(self, fname):
        self.fname = fname
        self.tags = ['ID', 'LAST NAME', 'FIRST NAME', 'CLASS', 'GPA']

    def openfile(self):
        with open(self.fname, 'r') as self.f:
            self.content = self.f.readlines()
    
    def format(self):
        for val in self.content:
            newlst = val.split(',')
            for index in range(5):
                print(self.tags[index], ':', newlst[index])



bag1 = Student('/Users/puhal/Documents/Python/DSA/Chapter1/StudentsDB.txt')

bag1.openfile()
bag1.format()