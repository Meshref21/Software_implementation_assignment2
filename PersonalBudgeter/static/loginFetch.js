let userInput = document.getElementById("user_input");

if(userInput)
{
userInput.addEventListener('submit', async (e) => {

    e.preventDefault();

    const inputForm = new FormData(userInput);

    const email = inputForm.get('email');
    const password = inputForm.get('password');

    const response = await fetch("http://127.0.0.1:8000/api/userinformation/", {
        method: 'GET'
    });

    const apiResponseArray = await response.json();

    const match = apiResponseArray.find(user => {
    return user.email === email && user.password === password;
    });

    if (match) 
    {
        window.location.href = "/home";
    } 
    else 
    {
        console.log("Invalid credentials");
    }

})}