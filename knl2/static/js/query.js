// selecting the :root theme
const root_theme = document.querySelector(':root');

// seleting the button which will trigger the event
const root_btn = document.querySelector('.watch-btn play-btn');

// the event listener to change the text color upon 'click'
root_btn.addEventListener('click', () => {
    // changing the color from #0b32e7 to #f44336
    root_theme.style.setProperty('--demo-color-change', '#f44336'); 
});