class computer:

    def __init__(self):
        self.name = 'Anon'
        self.age = 25

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = computer()
c1.age = 28
c2 = computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)

