public class StudentTest{
    public static void main(String[] args) {
        // Create an instance of Student
        Student student_1 = new Student
        ("Joe", "57");

        // Test your methods
        student_1.addCredits(10);   
        System.out.println(student_1.getCredits());
        System.out.println(student_1.getLoginName());


    }
}
