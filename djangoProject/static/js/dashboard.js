// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    const isAuthenticated = window.isAuthenticated;

    // use example data if user is not authenticated
    const childNames = isAuthenticated ? window.childNames : ['Alice', 'Bob', 'Charlie','Hugh','Charlotte', 'Susan', 'Kabul'];
    const dataLogsPerChild = isAuthenticated ? window.dataLogsPerChild : [5,0,1,9,10,12,7];

    const logCategories = isAuthenticated ? window.logCategories : ['Sleep', 'Food', 'Growth'];
    const logCategoryCounts = isAuthenticated ? window.logCategoryCounts : [9, 7, 12];

    // lots of extra colours to accommodate extra data
    const colours = [
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
        'rgb(64, 255, 159)',
    ]

    // pie chart
    const ctx1 = document.getElementById('pieChart');
    new Chart(ctx1, {
        type: 'doughnut',
        data: {
            labels: childNames,
            datasets: [{
                label: 'Logs',
                data: dataLogsPerChild,
                backgroundColor: colours,
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

    // bar chart
    const barChartCanvas = document.getElementById('barChart');
    if (barChartCanvas) {
        new Chart(barChartCanvas, {
            type: 'bar',
            data: {
                labels: logCategories,
                datasets: [{
                    label: 'Total Logs Per Category',
                    data: logCategoryCounts,
                    backgroundColor: colours,
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
                            // ski[p every second tick]
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

