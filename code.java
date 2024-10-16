
import java.util.Scanner;

/**
 * code
 */
public class code {

    public static void main(String[] args) {

        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Enter your Number: ");
            int num = input.nextInt();
            System.out.println("The table of " + num + " is: ");
            for (int i = 1; i <= 10; i++) {
                System.out.println(num + " X " + i + " = " + num * i);
            }
        }

        System.out.println("=== Code Execution Successful ===");
    }
}
