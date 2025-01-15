
const sidebar = document.getElementById('sidebar');

sidebar.addEventListener('mouseleave', () => {
    hoverTimeout = setTimeout(() => {
        sidebar.classList.remove('open');
    }, 200);
});

sidebar.addEventListener('mouseenter', () => {
    sidebar.classList.add('open');
});

