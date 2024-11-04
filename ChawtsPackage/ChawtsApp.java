package ChawtsPackage;

import javax.swing.JFrame;

public class ChawtsApp {
    public ChawtsApp(){}

    public static void main(String[] args) {
        //String sampleDataPath = "dataFilePath.csv" // change this to if we store data locally or on the web
        ChawtsData chawtsData = new ChawtsData(/*sampleDataPath*/);

        JFrame frame = new JFrame("Chawts"); // Title of the window that is opened
        ChawtsDisplay chawtsDisplay = new ChawtsDisplay(chawtsData);
        frame.getContentPane().add(chawtsDisplay);

        frame.setSize(1000, 1000);
        frame.setDefaultCloseOperation(3);
        frame.setVisible(true);
    }
}
