package ChawtsPackage;

import javax.swing.JFrame;

public class ChawtsApp {
    public ChawtsApp(){}

    public static void main(String[] args) {
        //String sampleDataPath = "dataFilePath.csv"
        ChawtsData chawtsData = new ChawtsData(/*sampleDataPath*/);
        //chawtsData.readFile();

        JFrame frame = new JFrame("Chawts");
        ChawtsDisplay chawtsDisplay = new ChawtsDisplay(chawtsData);
        frame.getContentPane().add(chawtsDisplay);

        frame.setSize(1000, 1000);
        frame.setDefaultCloseOperation(3);
        frame.setVisible(true);
    }
}
