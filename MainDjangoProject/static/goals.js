function showSection(sectionId) {
    ['goal-list-section', 'create-goal-section'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = 'none';
    });
    const target = document.getElementById(sectionId);
    if (target) target.style.display = sectionId === 'goals-grid' ? 'grid' : 'block';
}

function confirmDelete() {
    return confirm('Are you sure you want to delete this goal?');
}

function initializePieCharts() {
    document.querySelectorAll('.goal-pie-chart').forEach(chart => {
        let progress = parseFloat(chart.dataset.progress) || 0;
        progress = Math.min(Math.max(progress, 0), 100);

        // Color based on progress
        let fillColor = '#f43f5e';   // red  < 33%
        if (progress >= 66) fillColor = '#10b981';  // green
        else if (progress >= 33) fillColor = '#f59e0b'; // amber

        chart.style.background = `conic-gradient(
            ${fillColor} 0% ${progress}%,
            #e2e8f0 ${progress}% 100%
        )`;
    });
}

function initializeGoalPage() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('show') === 'create') {
        showSection('create-goal-section');
    } else {
        showSection('goal-list-section');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    initializeGoalPage();
    initializePieCharts();
});
