class Square():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def kvadrat(self):
        self.P = self.a * 4

        self.S = (self.a**2)    
        return self.P,self.S
    
    



class Rectangle(Square):
    def __init__(self,a,b,square_2):
        super().__init__(a,b)
        self.square_2 = square_2

    def pryamougol(self):

        self.P_2 = ((self.a+self.b)*2)
        self.S_2 = (self.a*self.b)
        
        return self.P_2,self.S_2




class Triangle(Rectangle):
    def __init__(self, a, b, square_2,c):
        super().__init__(a,b, square_2)
        self.c = c

    def treugolnik(self):
        self.P_3 = (self.a+self.b+self.c)

        return self.P_3



if __name__ == '__main__':
    test = Square(13,11)
    print(test.kvadrat())

    test_2 = Rectangle(13,11,12)
    print(test_2.pryamougol())

    test_3 = Triangle(13,11,12,5)
    print(test_3.treugolnik())