class Rectangle:
    def cal(self,len,bre):
        self.l=len
        self.b=bre

    def calculate(self):
        c=self.l*self.b
        print("Area of rectangle is:",c)
r=Rectangle()
a=int(input("enter length:"))
b=int(input("enter breath:"))
r.cal(a,b)
r.calculate()