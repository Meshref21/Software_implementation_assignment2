function showSection(sectionId) {
    const goalListSection = document.getElementById('goal-list-section');
    const createGoalSection = document.getElementById('create-goal-section');

    if (goalListSection) {
        goalListSection.style.display = 'none';
    }

    if (createGoalSection) {
        createGoalSection.style.display = 'none';
    }

    const selectedSection = document.getElementById(sectionId);

    if (selectedSection) {
        selectedSection.style.display = 'block';
    }
}


function confirmDelete() {
    return confirm("Are you sure you want to delete this goal?");
}


function initializeGoalPage() {
    const urlParams = new URLSearchParams(window.location.search);

    if (urlParams.get('show') === 'create') {
        showSection('create-goal-section');
    } else {
        showSection('goal-list-section');
    }
}


function initializePieCharts() {
    const charts = document.querySelectorAll(".goal-pie-chart");

    charts.forEach(function (chart) {
        let progress = parseFloat(chart.dataset.progress);

        if (isNaN(progress)) {
            progress = 0;
        }

        if (progress < 0) {
            progress = 0;
        }

        if (progress > 100) {
            progress = 100;
        }

        chart.style.background = `conic-gradient(
            #4caf50 0% ${progress}%,
            #e0e0e0 ${progress}% 100%
        )`;
    });
}


document.addEventListener("DOMContentLoaded", function () {
    initializeGoalPage();
    initializePieCharts();
});