import java.util.List;
public class HistoryUI {
    // Map to 'displayTransactions' in SDS
    public void displayTransactions(List<Transaction> transactions) {
        for (Transaction t : transactions) {
            System.out.println(t.getDetails());
        }
    }

    // Map to 'filterResults' in SDS
    public void filterResults(String criteria, List<Transaction> all) {
        // Implementation for filtering by date or amount
    }
}