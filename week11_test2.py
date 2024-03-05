class stringcount:
    def __init__(self,):
        self.word_list = []
        
    def counts(self,length):
        List = []
        for i in range(0,len(self.word_list)):
            if len(self.word_list[i]) == length:
                List.append(self.word_list[i])
        return List
    
    def count_upper(self,s):
        return [w for w in self.word_list if s == w]
    
    
test = stringcount()
test.word_list =  ["an","dat","lisa","ask","baby","anna","birthday","supper","dad","kayak"]
print(test.word_list)