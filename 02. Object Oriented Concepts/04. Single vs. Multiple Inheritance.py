class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class CanFly:
    def fly(self):
        return "Flying high!"

class Bird(Animal, CanFly):
    def speak(self):
        return f"{self.name} says Chirp!"

if __name__ == "__main__":
    bird = Bird("Tweety")
    print(bird.speak())  # Tweety says Chirp!
    print(bird.fly())    # Flying high!
