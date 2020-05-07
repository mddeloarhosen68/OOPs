class A:   #Parent Class or Super Class

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1-A working.")

    def feature2(self):
        print("Feature 2 working.")
class B:                                    #Child Class or Sub Class

    def __init__(self):
        print("in B init")

    def feature3(self):
        print("Feature 1-B working.")

    def feature4(self):
        print("Feature 4 working.")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().feature2()

a1 = C() 
a1.feat()
