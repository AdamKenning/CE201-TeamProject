
const sidebar = document.getElementById('sidebar');
const bars = document.querySelector('.menu-item .fa-bars');
let hoverTimeout;

function isMobile(){
    // Credit : https://dev.to/timhuang/a-simple-way-to-detect-if-browser-is-on-a-mobile-device-with-javascript-44j3
    if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
        return true
    }
    else{
        return false
    }
}

if(isMobile()){
    bars.addEventListener('click', () => {
        if(sidebar.classList.contains('open')){
            sidebar.classList.remove('open');
        }else{
            sidebar.classList.add('open');
        }
    });
}else{
    sidebar.addEventListener('mouseenter', () => {
        clearTimeout(hoverTimeout);
        sidebar.classList.add('open');
    });

    sidebar.addEventListener('mouseleave', () => {
        hoverTimeout = setTimeout(() => {
            sidebar.classList.remove('open');
        }, 200);
    });
}





