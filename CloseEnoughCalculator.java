import javax.swing.*;

public class CloseEnoughCalculator {
    public static void main(String[] args) {
        /*JDialog dialog = new JDialog();
        dialog.setTitle("Hello, World!");
        dialog.add(new JLabel("I didn't do it without help of a fucking AI"));
        dialog.setSize(300,500);
        dialog.setVisible(true); */

        //default title and icon
        //JOptionPane object = new Object();
        JFrame frame = new JFrame("popup");
        JOptionPane.showMessageDialog(frame,
            "Eggs are not supposed to be green.");


        String inputValue = JOptionPane.showInputDialog("input value");
        System.out.println(inputValue);
    }
}