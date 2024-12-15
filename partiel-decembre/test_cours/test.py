class Polynome :
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def __add__(self, poly) :
        return Polynome(self.a + poly.a, self.b + poly.b, self.c + poly.c)
    def __str__(self):
        return str(self.a)+"x**2+"+str(self.b)+"x+"+str(self.c)
    
a = Polynome(1,2,3)
b = Polynome(1,0,1)

print(a+b)