class Elephant:
    def __init__(self):
        None
    def m1(self):
        print(" I am an Elephant m1()")
    
    def m2(self):
        print(" I am an Elephant m2()")
    
    def m3(self):
        print(" I am an Elephant m3()")

    
    def m4(self):
        print("")
    def __str__(self):
        self.m1() 
        self.m2() 
        self.m3()
        self.m4()
        return f'from Elephant'    
        
class Lion(Elephant):
    def m3(self):
        print(" I am a Lion m3()")
    
    def __str__(self):
        Elephant.__str__(self)
       # self.m3()
        return ' from Lion'    
        
class Tiger(Lion):
    def m1(self):
        print(" I am a Tiger m1()")
    
    def m2(self):
        print(" I am a Tiger m2()")
    def __str__(self):
        Lion.__str__(self)
        #self.m1()
        #self.m2()
        return f'from Tiger'    
        
class wolf(Tiger):
    def m4(self):
        print("I am a wolf m4()")
    def __str__(self):
        Tiger.__str__(self)
        return f' from wolf'    
        
        
if __name__ == '__main__':
    l=["Elephant","Lion","Tiger","wolf"]
    for each in range(len(l)):
        a=eval(l[each]+ "()")
        print("From an ",l[each])
        a.__str__()