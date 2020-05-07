class student:

    school = 'Primeasia'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):            #instance method
        return(self.m1 + self.m2 + self.m3)/3

    @classmethod             #class method
    def getschool(cls):
        return cls.school

    @staticmethod             #static method
    def info():
        print("This is student class.. in abc module")
    """def get(self):          #fetch or get the value called geter or accessor
        return self.m1

    def set(self,value):       #modity or set  the value called seter or mutator
        self.m1 = value"""




s1 = student(80,95,87)
s2 = student(58,74,66)

print("Average of S1:",s1.avg())
print("Average of S2:",s1.avg())
print(student.info())

