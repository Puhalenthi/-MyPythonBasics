class ToDo():
    def __init__(self):
        self.todo = []
    
    def add(self, task, priority):
        if self.todo != [] and priority >= 0:
            counter = 0
            length = len(self.todo)
            for i in self.todo:
                if i[1] < priority:
                    if counter == length - 1:
                        self.todo.insert(counter, [task, priority])
                        break
                elif i[1] == priority:
                    self.todo.insert(counter, [task, priority])
                    break
                elif i[1] > priority:
                    self.todo.insert(counter, [task, priority])
                    break
                counter += 1
        else:
            self.todo.append([task, priority])
        
        return self.todo
    
    def complete(self):
        self.todo.pop(0)
        return self.todo

list = ToDo()
print(list.add('HW', 3))
print(list.add('Math', 2))
print(list.add('English', 4))
print(list.add('Social Studies', 3))
print(list.add('Science', 2))
print(list.add('Gym', 1))
print(list.add('Lunch', 6))
print(list.add('Spanish', 3))
print(list.complete())
print(list.complete())
print(list.complete())
print(list.complete())
print(list.complete())
print(list.complete())