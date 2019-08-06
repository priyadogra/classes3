class Factorial:
    def fact(self,a):
        self.d=a
        print(self.fac(self.d))

    def fac(self,d):
        if d==1:
            return 1
        else:
            # print(d*self.fac(d-1))
            return d*self.fac(d-1)

x=Factorial()

x.fact(5)

