
let el = document.querySelectorAll('li');

el.forEach(a => {
    a.addEventListener('click', function() {
        el.forEach(btn => btn.classList.remove('active'));
    this.classList.add('active');
    console.log("item clicked");
    });
    
});




