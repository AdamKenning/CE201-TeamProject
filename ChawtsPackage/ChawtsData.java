package ChawtsPackage;

public class ChawtsData {
    private final String filePath;
    // add some datatype relevant to store whatever data we want

    public ChawtsData(String filePath) {
        this.filePath = filePath;
    }

    // overload the constructor if no filepath is given
    public ChawtsData(){
        this(null);
    }
}
