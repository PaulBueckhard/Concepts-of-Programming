class Animal {
    void speak() {
        System.out.println("Some generic animal sound");
    }
}

class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("Woof!");
    }
}

class Cat extends Animal {
    @Override
    void speak() {
        System.out.println("Meow!");
    }
}

class Calculator {
    // Method overloading
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        Animal dog = new Dog();
        Animal cat = new Cat();

        dog.speak();  // Woof!
        cat.speak();  // Meow!

        Calculator calc = new Calculator();
        System.out.println("Sum of integers: " + calc.add(5, 3));  // Sum of integers: 8
        System.out.println("Sum of doubles: " + calc.add(5.5, 3.2));  // Sum of doubles: 8.7
    }
}
