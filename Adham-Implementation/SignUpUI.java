public class SignUpUI {
    private AuthenticationService authService;
    public SignUpUI(AuthenticationService service) {
        this.authService = service;
    }

    public void handleSignUp(String email, String pass) {
        if (authService.validateInput(email, pass)) {
            String hashed = authService.hashPassword(pass);
            User newUser = new User(email, hashed);
            authService.register(newUser);
            System.out.println("Registration Successful");
        } else {
            System.out.println("Error: Invalid Input");
        }
    }
}