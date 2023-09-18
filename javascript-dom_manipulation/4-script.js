var add_item = document.getElementById('add_item')

add_item.addEventListener('click', function(){
    var element = document.createElement('li');
    
    element.textContent = "Item";

    var my_list = document.querySelector('.my_list');

    my_list.appendChild(element)
})
