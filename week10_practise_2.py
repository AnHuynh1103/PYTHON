class Product:
    def __init__(self,name,amount,price):
        self.name = name
        self.amount = int(amount)
        self.price = float(price)
        print("Name of product:",self.name,",","product in stocks:",self.amount)

    def get_price(self,n):
        while self.amount and n > 0:
            if n < 10:
                self.cost = n*self.price
                print("Price of good is:",self.cost)
                return self.cost
            elif 10 <= self.amount <= 99:
                self.cost = n*self.price*0.9
                print("Price of good is:",self.cost)
                return self.cost
            else:
                self.cost = n*self.price*0.8
                print("Price of good is:",self.cost)
                return self.cost
        print("Please enter the product amounts: > 0 !!!")

    def make_purchase(self,n):
        while self.amount and n > 0:
            while n > self.amount:
                    print("Can't calculate!\nPleas enter n > amount!")
            print("Product to buy :",n)
            print("Product left in stocks:",self.amount - n)
            print("Final costs:",self.cost)
            return self.amount
        print("Please enter the product amounts: > 0 !!!")



#A = Product("sua tuoi",18,7000)
#A.get_price(8)
#A.make_purchase(8)

#B = Product("Cam",50,3000)
#B.get_price(14)
#B.make_purchase(14)


#C = Product("sua tuoi",int(input("Amount of products:\n"),int(input("Price of products:\n"))))
#C.get_price(2)
#C.make_purchase(2)

D = Product(input("Please enter the name of the good: \n"),input("Please enter the number of the good: \n"),input("Please enter the price: \n"))
D.get_price(int(input("Number of good you want to know price: \n")))
D.make_purchase(float(input("Number you want to buy: \n")))