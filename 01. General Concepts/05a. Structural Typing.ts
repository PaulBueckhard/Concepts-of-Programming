interface Point {
    x: number;
    y: number;
}

interface NamedPoint {
    x: number;
    y: number;
    name: string;
}

function printPoint(point: Point): void {
    console.log(`Point coordinates are (${point.x}, ${point.y})`);
}

const p1 = { x: 10, y: 20 };
const p2 = { x: 5, y: 15, name: "Origin" };

printPoint(p1);  // Valid
printPoint(p2);  // Valid due to structural typing
