public class GarbageCollectionExample {
    public static void main(String[] args) {
        GarbageCollectionExample obj = new GarbageCollectionExample();
        obj = null;  // The object is now eligible for garbage collection
        System.gc();  // Requesting garbage collection
    }

    @Override
    protected void finalize() throws Throwable {
        System.out.println("Garbage collection is performed.");
    }
}
