document.getElementById('hamburger').addEventListener('click', function() {
    const nav = document.getElementById('nav');
    nav.classList.toggle('active');
});

let lastScrollTop = 0;
const header = document.querySelector('header');

window.addEventListener('scroll', function() {
    
    if (window.innerWidth <= 500) {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        
        if (scrollTop > lastScrollTop) {
            
            header.classList.add('hidden');
        } else {
            
            header.classList.remove('hidden');
        }
        lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; 
    }
});
