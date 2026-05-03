let userInput = document.getElementById("input_date_form");
let apiResponse = "";
let filteredArray = [];
let chartInstance = null;

userInput.addEventListener('submit', async (e) => {

    e.preventDefault();

    const response = await fetch("http://127.0.0.1:8000/api/transaction/", {
        method: 'GET'
    });

    const apiResponse = await response.json();
    console.log(apiResponse);

    const startDate = document.getElementById("start_date").value;
    const endDate = document.getElementById("end_date").value;
    
    const startDateObject = new Date(startDate || "1900-01-01");
    const endDateObject = new Date(endDate || "2999-12-31");

    endDateObject.setHours(23, 59, 59, 999);

    filteredArray = apiResponse.filter(item => {
    const date = new Date(item.transactionDate);
    return date >= startDateObject && date <= endDateObject;
    });


    console.log(filteredArray);

        const totals = {};
    filteredArray.forEach(item => {
        totals[item.category] = (totals[item.category] || 0) + Number(item.amount);
    });

    const labels = Object.keys(totals);
    const data = Object.values(totals);

    renderPieChart(labels, data);


})

function renderPieChart(labels, data) {
    const ctx = document.getElementById('myChart').getContext('2d');

    if (chartInstance) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: [
                    '#FF6384',
                    '#36A2EB',
                    '#FFCE56',
                    '#4BC0C0',
                    '#9966FF',
                    '#FF9F40',
                    '#C9CBCF'
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom' },
                title: {
                    display: true,
                    text: 'Amount by Category'
                }
            }
        }
    });
}

