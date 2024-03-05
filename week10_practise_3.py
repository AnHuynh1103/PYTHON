class Password_manager:
    def __init__(self):
        self.listpass = ["Soicon123"]
    
    def get_pass(self):
        return print('Current password: ',self.listpass[-1])
    
    def set_pass(self,new_pass):
        if new_pass not in self.listpass:
            self.listpass.append(new_pass)
            return print("OK")
        else:
            return print("Try again. Same current password!")
        
    def is_correct(self,login_pass):
        if self.listpass[-1] == login_pass:
            return print(True)
        else:
            return print(False)
            
        
        
A = Password_manager()  
A.set_pass(input("Please enter your new password:\n"))
A.get_pass()
A.is_correct(input("Please enter your current password:\n"))
