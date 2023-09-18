var update_header = document.getElementById('update_header')

update_header.addEventListener('click', function(){
    var header = document.querySelector('header');

    header.textContent = "New Header!!!"
})
