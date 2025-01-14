const sidebar = document.getElementById('sidebar');

// function toggleSidebar() {
//     console.log('Toggling sidebar'); 
//     const sidebar = document.getElementById('sidebar');
//     sidebar.classList.toggle('open');
// }

sidebar.addEventListener('mouseleave', () => {
    hoverTimeout = setTimeout(() => {
        sidebar.classList.remove('open');
    }, 200);
});

sidebar.addEventListener('mouseenter', () => {
    sidebar.classList.add('open');
});

