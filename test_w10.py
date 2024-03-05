import random

class ROCK_PAPER_SCRISSORS():
    def __init__(self):
        self.method = ["Keo","Bua","Bao"]
        self.round = 5
        self.player_win = 0
        self.com_win = 0
        self.current_round = 0
        
    def choose_player_method(self,method):
        self.player_method = method
        
    def compare(self):
        self.com_method = random.choice(self.method)
        self.current_round += 1

        print("Tong so vong: ",self.round)
        print("Vong hien tai: ",self.current_round)
        print("Player chon: ",self.player_method)
        print("Com chon: ",self.com_method)
        
        if self.player_method == self.com_method:
            print("draw")
            
        elif self.player_method == "Keo":
            if self.com_method == "Bao":
                print("Player win!")
                self.player_win += 1
            else:
                print("Player lose!")
                self.com_win += 1
                
        elif self.player_method == "Bua":
            if self.com_method == "Keo":
                print("Player win!")
                self.player_win += 1
            else:
                print("Player lose!")
                self.com_win += 1
                
        elif self.player_method == "Bao":
            if self.com_method == "Bua":
                print("Player win!")
                self.player_win += 1
            else:
                print("Player lose!")
                self.com_win += 1
                
        if self.current_round == self.round:
            print("")
            print("Player win: ",self.player_win,"---COM win",self.com_win,"draw",self.round - self.com_win - self.player_win)
            
            if self.player_win > self.com_win:
                print("Ket qua BO5: player win")
            elif self.player_win < self.com_win:
                print("Ket qua BO5: com win")
            else:
                print("draw")
            print("")
            
def show_com_method(self):
    print("show func com choose: ",self.com_method)
    
#
game = ROCK_PAPER_SCRISSORS()
game.choose_player_method(input("Hay chon [Keo, Bua, Bao]:"))
game.compare()
#

#
game.choose_player_method(input("Hay chon [Keo, Bua, Bao]:"))
game.compare()
#

#
game.choose_player_method(input("Hay chon [Keo, Bua, Bao]:"))
game.compare()
#

#
game.choose_player_method(input("Hay chon [Keo, Bua, Bao]:"))
game.compare()
#

#
game.choose_player_method(input("Hay chon [Keo, Bua, Bao]:"))
game.compare()
#