from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("It's Running")

#com = Computer()
com1 = Laptop()
#com.process()
com1.process()
