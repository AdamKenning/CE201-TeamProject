package ChawtsPackage;

import javax.swing.*;
import java.awt.*;

public class ChawtsDisplay extends JComponent {
    private final ChawtsData chawtsData;

    public ChawtsDisplay(ChawtsData chawtsData){
        this.chawtsData = chawtsData;
    }

    protected void paintComponent(Graphics graphics) {
        Graphics2D g = (Graphics2D)graphics;

        g.drawOval(0,0,getWidth(),getHeight());
    }
}


