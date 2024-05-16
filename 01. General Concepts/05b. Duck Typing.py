class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm a person, but I can quack like a duck!")

def make_it_quack(duck):
    duck.quack()

d = Duck()
p = Person()

make_it_quack(d)  # Valid
make_it_quack(p)  # Valid due to duck typing
