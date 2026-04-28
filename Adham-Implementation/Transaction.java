public class Transaction {
    private double amount;
    private String date;
    private String description;

    public String getDetails() {
        return date + ": " + description + " (" + amount + ")";
    }
}