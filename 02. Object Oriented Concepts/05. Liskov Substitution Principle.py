class Bird:
    def fly(self):
        return "Flying high!"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying low!"

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly!")

def make_bird_fly(bird: Bird):
    return bird.fly()

if __name__ == "__main__":
    sparrow = Sparrow()
    ostrich = Ostrich()

    print(make_bird_fly(sparrow))  # Sparrow flying low!

    # The following line will raise an exception as per LSP violation
    # print(make_bird_fly(ostrich))  # NotImplementedError: Ostriches can't fly!
