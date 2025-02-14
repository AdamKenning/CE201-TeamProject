// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    const ctx1 = document.getElementById('pieChart');
    new Chart(ctx1, {
        type: 'doughnut',
        data: {
            labels: window.childNames,  // global JS variable from Django
            datasets: [{
                label: 'Logs',
                data: window.dataLogsPerChild,
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(153, 102, 255)',
                    'rgb(255, 159, 64)',
                    'rgb(132, 255, 99)',
                    'rgb(235, 54, 54)',
                    'rgb(86, 255, 205)',
                    'rgb(192, 75, 192)',
                    'rgb(255, 153, 102)',
                    'rgb(64, 255, 159)'
                ],
                hoverOffset: 15,
            }]
        },
        options: {
            maintainAspectRatio: false,
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Logs Per Child',
                    font: {
                        size: 20
                    }
                }
            }
        }
    });

    const barChartCanvas = document.getElementById('barChart');
    if (barChartCanvas) {
        new Chart(barChartCanvas, {
            type: 'bar',
            data: {
                labels: window.logCategories,
                datasets: [{
                    label: 'Total Logs Per Category',
                    data: window.logCategoryCounts,
                    backgroundColor: ['#ff6384', '#36a2eb', '#ffce56'],
                    hoverOffset: 50,
                }]
            },
            options: {
                maintainAspectRatio: false,
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: (val, index) => {
                                return index % 2 === 0 ? val : undefined;
                              },
                            font: {
                                size: 14
                            }
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Logs Per Category',
                        font: {
                            size: 20
                        }
                    },
                    legend: {
                        display: false
                    }
                }
            }
        });
    }
});

