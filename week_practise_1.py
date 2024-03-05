class Invesment:
    def __init__(self, principal, interest) -> None:
        self.principal = principal
        self.interest = interest
        
    def value_after(self):
        n = int(input("Number of the years:\n"))
        self.value = self.principal*((self.interest)/100+1)**n
        self.value = round(self.value,2)
        return self.value
        
        

A = Invesment(float(input("The principal amount:\n")),float(input("The interest (%):\n")))
print("The final value: ",A.value_after())