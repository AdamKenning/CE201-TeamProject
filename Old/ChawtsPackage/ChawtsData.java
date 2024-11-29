package ChawtsPackage;

public class ChawtsData {
    private final String filePath;
    // add some datatype relevant to store whatever data we want

    public ChawtsData(String filePath) {
        this.filePath = filePath;

        // call read file immediately after initialization
        readFile();
    }

    // overload the constructor if no filepath is given
    public ChawtsData(){this(null);}

    private String getFilePath(){return this.filePath;}

    public void readFile() {
        String filePath = getFilePath();
        // do something to read file and populate ChawtsData with data ?
    }
}
