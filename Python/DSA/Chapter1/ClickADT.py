class click:
    def __init__(self):
        self.counter = 0

    def click(self):
        self.counter += 1
        return self.counter
    
    def reset(self):
        self.counter = 0
        return self.counter


button = click()
for _ in range(5):
    for _ in range(10):
        print(button.click())
    print(button.reset())