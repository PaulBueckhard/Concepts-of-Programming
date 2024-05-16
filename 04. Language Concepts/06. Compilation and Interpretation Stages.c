#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int sum = a + b;
    printf("Sum: %d\n", sum);
    return 0;
}

// Scanning/Lexing: The lexer converts the sequence of characters into tokens like int, main, =, 5, ;, etc.

// Parsing: The parser generates an abstract syntax tree from the tokens. The AST represents the grammatical structure of the source code.

// Semantic Analysis: The compiler checks for semantic errors such as type mismatches, variable declarations, and scope rules. It also performs type checking and ensures that the operations are valid for the given types.

// Code Generation: The compiler translates the AST and semantic information into machine code or an intermediate representation. In this case, gcc generates machine code for the target architecture.

// Running: The resulting executable file can be run directly on the hardware.