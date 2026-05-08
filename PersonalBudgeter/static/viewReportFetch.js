let chartInstance = null;

const COLORS = [
    '#6366f1', '#10b981', '#f43f5e', '#f59e0b',
    '#3b82f6', '#8b5cf6', '#ec4899', '#14b8a6'
];

document.getElementById('input_date_form').addEventListener('submit', async (e) => {
    e.preventDefault();
    await generateReport();
});

async function generateReport() {
    const startDate   = document.getElementById('start_date').value;
    const endDate     = document.getElementById('end_date').value;
    const chartType   = document.getElementById('chart-type').value;
    const filterType  = document.getElementById('filter-type').value;

    try {
        const res = await fetch('/api/transaction/');
        const all = await res.json();

        const startObj = new Date(startDate || '1900-01-01');
        const endObj   = new Date(endDate   || '2999-12-31');
        endObj.setHours(23, 59, 59, 999);

        let filtered = all.filter(t => {
            const d = new Date(t.transactionDate);
            return d >= startObj && d <= endObj;
        });

        if (filterType === 'expense') filtered = filtered.filter(t => !t.isIncome);
        if (filterType === 'income')  filtered = filtered.filter(t =>  t.isIncome);

        // Summary stats
        let income = 0, expense = 0;
        all.filter(t => {
            const d = new Date(t.transactionDate);
            return d >= startObj && d <= endObj;
        }).forEach(t => {
            if (t.isIncome) income += parseFloat(t.amount);
            else            expense += parseFloat(t.amount);
        });

        document.getElementById('rpt-income').textContent  = '$' + income.toFixed(2);
        document.getElementById('rpt-expense').textContent = '$' + expense.toFixed(2);
        document.getElementById('rpt-count').textContent   = filtered.length;
        document.getElementById('report-summary').style.display = 'grid';

        // Totals by category
        const totals = {};
        const counts = {};
        filtered.forEach(t => {
            totals[t.category] = (totals[t.category] || 0) + parseFloat(t.amount);
            counts[t.category] = (counts[t.category] || 0) + 1;
        });

        const labels = Object.keys(totals);
        const data   = Object.values(totals);
        const total  = data.reduce((a, b) => a + b, 0);

        if (labels.length === 0) {
            document.getElementById('chart-placeholder').style.display = 'block';
            document.getElementById('chart-placeholder').innerHTML =
                '<div class="icon">🔍</div><p>No transactions found for this range.</p>';
            document.getElementById('chart-wrapper').style.display = 'none';
            document.getElementById('breakdown-card').style.display = 'none';
            return;
        }

        // Update chart title
        const rangeText = startDate && endDate
            ? `${startDate} → ${endDate}`
            : 'All Time';
        document.getElementById('chart-subtitle').textContent = rangeText;

        renderChart(labels, data, chartType);

        // Breakdown table
        const tbody = document.getElementById('breakdown-tbody');
        tbody.innerHTML = labels.map((cat, i) => `
            <tr>
                <td class="fw-600">${cat.charAt(0).toUpperCase() + cat.slice(1)}</td>
                <td>${counts[cat]}</td>
                <td class="fw-600">$${data[i].toFixed(2)}</td>
                <td>
                    <div style="display:flex; align-items:center; gap:0.5rem;">
                        <div style="flex:1; background:#f1f5f9; border-radius:999px; height:6px; overflow:hidden;">
                            <div style="width:${((data[i]/total)*100).toFixed(1)}%; height:100%; background:${COLORS[i % COLORS.length]}; border-radius:999px;"></div>
                        </div>
                        <span style="font-size:0.8rem; color:var(--text-muted); min-width:36px;">
                            ${((data[i]/total)*100).toFixed(1)}%
                        </span>
                    </div>
                </td>
            </tr>
        `).join('');
        document.getElementById('breakdown-card').style.display = 'block';

    } catch (err) {
        console.error('Report error:', err);
    }
}

function renderChart(labels, data, type) {
    document.getElementById('chart-placeholder').style.display = 'none';
    document.getElementById('chart-wrapper').style.display = 'block';

    const ctx = document.getElementById('myChart').getContext('2d');
    if (chartInstance) chartInstance.destroy();

    chartInstance = new Chart(ctx, {
        type: type,
        data: {
            labels: labels.map(l => l.charAt(0).toUpperCase() + l.slice(1)),
            datasets: [{
                data: data,
                backgroundColor: COLORS.slice(0, data.length),
                borderWidth: type === 'bar' ? 0 : 2,
                borderColor: '#fff',
                borderRadius: type === 'bar' ? 6 : 0,
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: type === 'bar' ? 'top' : 'bottom',
                    labels: { font: { family: 'Inter', size: 12 }, padding: 16 }
                },
                title: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: (ctx) => ` $${ctx.parsed.toFixed ? ctx.parsed.toFixed(2) : ctx.parsed.y.toFixed(2)}`
                    }
                }
            },
            scales: type === 'bar' ? {
                y: {
                    beginAtZero: true,
                    grid: { color: '#f1f5f9' },
                    ticks: { callback: v => '$' + v }
                },
                x: { grid: { display: false } }
            } : {}
        }
    });
}
