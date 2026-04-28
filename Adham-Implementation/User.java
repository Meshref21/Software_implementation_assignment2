public class User {
    private int id;
    private String name;
    private String email;
    private String password;
    private String currency;

    public User(String email, String password) {
        this.email = email;
        this.password = password;
        
    }

    // Map to 'hashPassword' logic in Sequence Diagram 1
    public void setHashedPassword(String hashedPass) {
        this.password = hashedPass;
    }
}
