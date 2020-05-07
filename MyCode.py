class computer():

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
 
    def config(self):
        print("Config is ", self.cpu, self.ram)


com1 = computer('i5',16)
com2 = computer('i7',32)


com1.config()     #computer.config(com1)
com2.config()     #computer.config(com2)


