function add(a: number, b: number): number {
    return a + b;
}

// Both integers
let resultInt: number = add(10, 5);
console.log("Adding integers:", resultInt);

// Both floats
let resultFloat: number = add(10.5, 5.5);
console.log("Adding floats:", resultFloat);

// Uncommenting the following lines will result in compile-time errors
// let resultMixed = add("Hello", 5); // Error: Argument of type 'string' is not assignable to parameter of type 'number'.
// let resultString = add("Hello", " World!"); // Error: Argument of type 'string' is not assignable to parameter of type 'number'.

// Example showing type safety
function processData(data: number | string | number[]): void {
    console.log("Processing data:", data);
}

// Different types of data can be passed to the function with type annotations
processData(42);
processData(3.14);
processData("A statically typed string");
processData([1, 2, 3, 4]);

// Uncommenting the following line will result in a compile-time error
// processData({ key: "value" }); // Error: Argument of type '{ key: string; }' is not assignable to parameter of type 'number | string | number[]'.
