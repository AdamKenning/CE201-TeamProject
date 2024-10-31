package ChawtsPackage;

public class ChawtsData {
    private final String filePath;

    public ChawtsData(String filePath) {
        this.filePath = filePath;
    }

    // overload the constructor if no filepath is given
    public ChawtsData(){
        this(null);
    }
}
