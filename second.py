class Add:
    def sum(self,a,b):
        self.c=a
        self.d=b
    def sums(self):
        e=self.c+self.d
        print(e)
        return e
x=Add()
f=int(input("enter value:"))
g=int(input("enter value:"))
x.sum(f,g)
d=x.sums()
print(d)
