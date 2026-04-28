public class AuthenticationService {
    // Linked to 'validateInput' and 'hashPassword' in SDS
    public boolean validateInput(String email, String pass) {
        return email.contains("@") && pass.length() > 6;
    }

    public String hashPassword(String pass) {
        return "hashed_" + pass;
    }

    public void register(User u) {
        Database.saveNewUser(u);
    }
}