#include <iostream>

class Example {
public:
    Example() { std::cout << "Object created\n"; }
    ~Example() { std::cout << "Object destroyed\n"; }
};

void createExample() {
    Example ex; // Object is created here
} // Object is destroyed automatically when it goes out of scope

int main() {
    createExample();
    return 0;
}
