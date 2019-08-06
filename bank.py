c = int(input("Enter total amount:"))
class Bank:
    def bank(self):
        print("press 1 for deposit:")
        print("press 2 for withdraw:")
        self.a=int(input("Enter your choice:"))

    def first(self):

        while(True):
            global c

            if self.a==1:
                d=int(input("Enter  amount u want to deposit:"))
                c=c+d
                print("Total amount is:",c)
            elif self.a==2:
                e=int(input("Enter amount u want to withdraw:"))
                c=c-e
                print("Total amount is :",c)
            else:
                print("choose right option")
            z=input("Do you want to continue y for yes / n for no")
            if z=='y':
                self.bank()
            elif z=='n':
                break
b=Bank()
b.bank()
b.first()