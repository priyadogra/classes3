class Target:

    def calculate(self,a,b):
        a=50
        b=[10,20,30,40]

        for i in range(len(b)):
            if a==b[i]+b[i+1]:
                print(b[i])
t=Target()
t.calculate()