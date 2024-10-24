package SandBox.src;
public class BooleanChecker {

    // Method to check if both values are the same
    public boolean bothSameValue(boolean a, boolean b) {
        return a == b;
    }

    // Method to check if only one value is true
    public boolean onlyOneTrue(boolean a, boolean b) {
        return a != b;
    }

    public static void main(String[] args) {
        BooleanChecker checker = new BooleanChecker();

        System.out.println(checker.bothSameValue(true, true)); // Output: true
        System.out.println(checker.bothSameValue(true, false)); // Output: false
        System.out.println(checker.onlyOneTrue(true, false)); // Output: true
        System.out.println(checker.onlyOneTrue(false, false)); // Output: false
    }
}
