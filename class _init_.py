class strq:
    def __init__(self):
        self.uc=0
        self.lc=0
        self.sp=0
        self.vow=0
        self.cons=0
        self.string=""
    def getstr(self):
        self.string=str(input("enter the string"))
    def cuc(self):
        for ch in self.string:
            if(ch.isupper()):
                self.uc+=1
    def clc(self):
        for lc in self.string:
            if(ch.islower()):
                self.lc+=1
    def csp(self):
        for sp in self.string:
            if ch=="":
                self.sp+=1
    def cvow(self):
        for ch in self.string:
            if(ch in ('A','E','I','O','U','a','e','i','o','u')):
                self.vow+=1
    def ccons(self):
        for ch in self.string:
            if(ch not in('A','E','I','O','U','a','e','i','o','u')):
                self.cons+=1
    def execute(self):
        self.cuc()
        self.clc()
        self.csp()
        self.cvow()
        self.ccons()
    def display(self):
        print("the given string has\n")
        print("uppercase",self.up)
        print("llowercase",self.lc)
        print("space",self.sp)
        print("vowles",self.vow)
        print("consonants",self.cons)

lc.clc()
uc.cuc()
sp.csp()
vow.cvow()
cons.ccons()
