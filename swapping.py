class Swap:
    def swap(self):
        self.a=int(input("enter value of a:"))
        self.b=int(input("enter value of b:"))
        self.first(self.a,self.b)
    def first(self,a,b):

        c=0
        c=b
        b=a
        a=c
        print(a)
        print(b)

s=Swap()
s.swap()
