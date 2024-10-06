package SandBox.src;

public class Main {
    public static void main(String[] args) {
        // Create an instance of TicketMachine
        TicketMachine machine = new TicketMachine(500);

        // Test your methods
        machine.insertMoney(300);
        machine.printTicket();
        System.out.println("Balance: " + machine.getBalance());

        // Calculate saving for a 20% discount
        double discount = 0.2;
        double saving = machine.calculateSaving(discount);
        System.out.println("You saved: " + saving + " from a discount of " + (discount * 100) + "% on the price of "
                + machine.getPrice());
    }
}
