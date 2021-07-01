
class Animal():
    def __init__(self) -> None:
        pass

    def move(self):
        raise NotImplementedError()

    def eat(self,name:str):
        print("{0} Eating".format(name))


class Dog(Animal):

    def __init__(self, name: str, age: int) -> None:
        self.Name=name
        self.Age=age
        Animal.__init__(self);
    
    def eat(self):
        super().eat(self.Name)

    def move(self):
        print("{0} Walks".format(self.Name))

class Fish(Animal):
    def __init__(self, name: str, age: int) -> None:
        self.Name=name
        self.Age=age
        super().__init__()
    
    def eat(self):
        super().eat(self.Name)
    
    def move(self):
       print("{0} Swims".format(self.Name))

class Bird(Animal):
    def __init__(self, name: str, age: int) -> None:
        self.Name=name
        self.Age=age
        super().__init__()


    def eat(self):
        super().eat(self.Name)
    
    def move(self):
       print("{0} Flys".format(self.Name))






if __name__=='__main__' :
    dog= Dog("Rolf",4)
    fish=Fish('golden',1)
    bird=Bird('Eagle',20)


    dog.move()
    dog.eat()

    fish.move()
    fish.eat()


    bird.move()
    bird.eat()





