let navContent = document.querySelector('.nav-content');
let menuBar = document.querySelector('.menu-bar');
let closeMenuBar = document.querySelector('.close-menu-bar');

menuBar.addEventListener('click', () => {
    navContent.classList.toggle('show-nav');
    menuBar.style.display = 'none';
});

closeMenuBar.addEventListener('click', () => {
    navContent.classList.remove('show-nav');
    menuBar.style.display = 'flex';
});

let searchIcon = document.querySelector('.search-icon');
let search = document.querySelector('.search');
let closeSearch = document.querySelector('.close-search');

searchIcon.addEventListener('click', () => {
    search.classList.toggle('show-search-bar');
});

closeSearch.addEventListener('click', () => {
    search.classList.toggle('show-search-bar');
})