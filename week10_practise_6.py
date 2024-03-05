class Converter:
    def __init__(self,length,unit):
        self.length = length
        self.unit = unit
        self.dict = {"inches" : 1,
                     "yards" : 1/36,
                     "feet" : 1/12,
                     "miles" : 1/63360,
                     "kilometers" : 1/39370.0787,
                     "meters" : 1/39.3700787,
                     "centimeters" : 1/0.393700787,
                     "millimeters" : 1/0.0393700787}
        
    def inches(self):
        print("Convert to inches")
        return self.length*self.dict['inches']/self.dict[self.unit]
    def yards(self):
        print("Convert to yards")
        return self.length*self.dict['yards']/self.dict[self.unit]
    def feet(self):
        print("Convert to feet")
        return self.length*self.dict['feet']/self.dict[self.unit]
    def miles(self):
        print("Convert to miles")
        return self.length*self.dict['miles']/self.dict[self.unit]
    def kilometers(self):
        print("Convert to kilometers")
        print("So chia",self.dict[self.unit])
        return self.length*self.dict['kilometers']/self.dict[self.unit]
    def meters(self):
        print("Convert to meters")
        print("So chia",self.dict[self.unit])
        return self.length*self.dict['meters']/self.dict[self.unit]
    def centimeters(self):
        print("Convert to centimeters")
        print("So chia",self.dict[self.unit])
        return self.length*self.dict['centimeters']/self.dict[self.unit]
    def millimeters(self):
        print("Convert to millimeters")
        print("So chia",self.dict[self.unit])
        return self.length*self.dict['millimeters']/self.dict[self.unit]
    

#/self.dict[self.unit]
A = Converter(1,"inches")
print("Value after converted:\n",A.meters())
    