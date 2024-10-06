package SandBox.src;

public class Main {
    public static void main(String[] args) {
        // Create an instance of TicketMachine
        TicketMachine machine = new TicketMachine(500);

        // Test your methods
        machine.insertMoney(300);
        machine.printTicket();
        System.out.println("Balance: " + machine.getBalance());
    }
}
