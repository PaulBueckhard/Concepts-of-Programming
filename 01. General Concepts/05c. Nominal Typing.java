class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class NamedPoint extends Point {
    String name;

    NamedPoint(int x, int y, String name) {
        super(x, y);
        this.name = name;
    }
}

public class Main {
    public static void printPoint(Point point) {
        System.out.println("Point coordinates are (" + point.x + ", " + point.y + ")");
    }

    public static void main(String[] args) {
        Point p1 = new Point(10, 20);
        NamedPoint p2 = new NamedPoint(5, 15, "Origin");

        printPoint(p1);  // Valid
        printPoint(p2);  // Valid because NamedPoint is a subclass of Point
    }
}
