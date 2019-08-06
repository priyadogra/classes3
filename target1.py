lis=[10,20,30,40,5,15,25,25]
class Target:
    def target(self):
        self.t=int(input("Enter target value:"))
        self.first(self.t)

    def first(self,t):
        global lis

        for i in range(len(lis)-1):

            c=lis[i]+lis[i+1]

            if t==c:
                print("sum of",lis[i],"and",lis[i+1],"=",c)

t1=Target()
t1.target()
