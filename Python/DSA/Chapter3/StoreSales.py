class Sales:
    def __init__(self, url):
        with open(url, 'r') as f:
            self.file = f.readlines()
        
        self.totalsaleslist = []
    
    def SumByStore(self):
        for index in range(len(self.file)):
            if index % 2 == 0:
                print(self.file[index])
            else:
                numlist = self.file[index].split(' , ')
                for i in range(len(numlist)):
                    numlist[i] = float(numlist[i])
                
                val = self.add(numlist)
                self.totalsaleslist.append([self.file[index-1], val])
                print(val)
                print('+-----------------+')

    def add(self, list):
        counter = 0
        for i in list:
            counter += i
        
        return counter
    
    def storesByValue(self):
        if self.totalsaleslist == []:
            self.SumByStore()
        
        numlst = []
        for i in self.totalsaleslist:
            numlst.append(i[1])

        numlst.sort()
        
        storelst = []
        
        for i in numlst:
            for j in self.totalsaleslist:
                if i == j[1]:
                    storelst.append(j[0])
        
        return storelst


a = Sales('/Users/puhal/Documents/Python/DSA/Chapter3/StoreSales.txt')

print(a.storesByValue())