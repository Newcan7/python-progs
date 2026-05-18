class Complex:
    def __init__(self,x,y):
        self.real=x
        self.imag=y
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    def __add__(self, num2):
        newreal=self.real+num2.real
        newimag=self.imag+num2.imag
        return Complex(newreal,newimag)
        
num1= Complex(2,3)
print(num1)
num2=Complex(4,5)
print(num2)
num3=num1+num2
print(num3)
