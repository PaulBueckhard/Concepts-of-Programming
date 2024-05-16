import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class ReflectionExample {
    private String message;

    public ReflectionExample(String message) {
        this.message = message;
    }

    public void printMessage() {
        System.out.println("Message: " + message);
    }

    public static void main(String[] args) throws Exception {
        // Create an instance of ReflectionExample
        ReflectionExample obj = new ReflectionExample("Hello, World!");

        // Get the Class object associated with ReflectionExample
        Class<?> clazz = obj.getClass();

        // Inspect fields
        Field field = clazz.getDeclaredField("message");
        field.setAccessible(true);  // Make private field accessible
        System.out.println("Field name: " + field.getName());
        System.out.println("Field value: " + field.get(obj));

        // Modify the field value
        field.set(obj, "Hello, Reflection!");
        System.out.println("Modified field value: " + field.get(obj));

        // Inspect methods
        Method method = clazz.getMethod("printMessage");
        System.out.println("Method name: " + method.getName());

        // Invoke the method
        method.invoke(obj);
    }
}
