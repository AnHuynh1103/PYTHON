class Wordplay:
    def __init__(self):
        self.word_list = []
        
    def words_with_length(self,length):
        List = []
        for i in range(0,len(self.word_list)):
            if len(self.word_list[i]) == length:
                List.append(self.word_list[i])
        return List
    
    def starts_with(self,s):
        return [w for w in self.word_list if w[:len(s)] == s]
    
    def ends_with(self,s):
        return [w for w in self.word_list if w[::-1][:len(s)] == s[::-1]]
    
    def palindromes(self):
        List = [w for w in self.word_list if w[::-1] == w]
        return List
    
    def only(self,s):
        return [w for w in self.word_list if s in w]
    
    def avoid(self,s):
        return [w for w in self.word_list if s not in w]




test = Wordplay()
test.word_list = ["an","dat","lisa","ask","baby","anna","birthday","supper","dad","kayak"]

print("The list:",test.word_list)
print("Return a list of all words of length:",test.words_with_length(int(input("Enter the length of the word you want to take:\n"))))
print("Return a list of all words that start with:",test.starts_with(input("Enter the start character:\n").lower()))
print("Return a list of all words that end with:",test.ends_with(input("Enter the end character:\n").lower()))
print("Return a list of all palindromes in the list:",test.palindromes())
print("Return a list of the word thay contain only those letters:",test.only(input("Enter the only character:\n").lower()))
print("Return a list of the word thay contain none those letters:",test.avoid(input("Enter the avoid character:\n").lower()))