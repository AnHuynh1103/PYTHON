class Time:
    def __init__(self,seconds):
        self.seconds = seconds
        
    def convert_to_minutes(self):
        mins = self.seconds/60
        secs = self.seconds%60
        return print("Convert to minutes: %d:%d"%(mins,secs))
    
    def convert_to_hours(self):
        hours = self.seconds/3600
        mins = self.seconds%3600/60
        secs = self.seconds%60
        return print("Convert to hours: %d:%d:%d"%(hours,mins,secs))
    
    
A = Time(350)
A.convert_to_minutes()
A.convert_to_hours()
