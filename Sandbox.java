import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Sandbox {
    public static void main(String[] args) {
        JTextField firstName = new JTextField(15);
        JTextField age = new JTextField(15);

        String[] colors = {"Red", "Green", "Blue"};
        JComboBox<String> colorBox = new JComboBox<>(colors);

        JPanel panel = new JPanel();
        panel.add(new JLabel("First Name:"));
        panel.add(firstName);

        panel.add(new JLabel("Age:"));
        panel.add(age);

        panel.add(new JLabel("Favorite Color:"));
        panel.add(colorBox);

        int result = JOptionPane.showConfirmDialog(
                null,
                panel,
                "User Information",
                JOptionPane.OK_CANCEL_OPTION);

        if (result == JOptionPane.OK_OPTION) {
            System.out.println("Name: " + firstName.getText());
            System.out.println("Age: " + age.getText());
            System.out.println("Color: " + colorBox.getSelectedItem());
        }
    }
}
