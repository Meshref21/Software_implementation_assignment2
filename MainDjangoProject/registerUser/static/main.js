let userInput = document.getElementById("user_input");

if(userInput)
{
userInput.addEventListener('submit', async (e) => {

    e.preventDefault();

    const inputForm = new FormData(userInput);

    const response = await fetch("http://127.0.0.1:8000/api/userinformation/", {
        method: 'POST',
        body: inputForm
    });

    const apiResponse = await response.json();
    console.log(apiResponse);

})}