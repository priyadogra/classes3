b = 0
c = 1
d = 0
class  Fibbonici:
    def  fibbonici(self):


        self.a = int(input("enter range:"))

        self.first(self.a)

    def first(self,a):
        global b
        global c
        global d
        for i in range(a):
            if i > 2:
                d = b + c
                if d > a:
                    break
                print(d, ' ', end='')
                b = c
                c = d

            elif i == 0:
                print(0)

            elif i == 1:
                print(1)

f=Fibbonici()
f.fibbonici()