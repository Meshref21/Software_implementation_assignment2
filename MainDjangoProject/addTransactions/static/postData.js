fetch("http://127.0.0.1:8000/api/transaction/")
    .then(response =>   
    {
        if(!response.ok)
        {   
            throw new Error("Could not fetch resource")
        }
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error(error));

let userInput = document.getElementById("input_fields");

userInput.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);

    console.log(data);
})

async function fetchData() 
{
    try
    {
        const response = await fetch("http://127.0.0.1:8000/api/transaction/")

        if(!response.ok)
        {
            throw new Error("Could not fetch resource")
        }
        const data = await response.json();
        return data;
    }
    catch(error)
    {
        return error;
    }
}

const dataFromApi = fetchData();