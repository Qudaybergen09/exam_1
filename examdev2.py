class Shop():
    user = int(input('Buy: ')) 
    def __init__(self,name,descritption,quntw,summa):
        self.name = name
        self.description = descritption
        self.quntw = quntw
        self.summa = summa

    def obshaya(self):
        self.Porsche = 30000

        if self.user == 3:
            return self.user*self.Porsche
        elif self.user == 2:
            return self.user * self.Porsche
        
            

if __name__ == '__main__':
    a = Shop('Porsche','wheels', 2, 30000)
    print(a.obshaya())
    