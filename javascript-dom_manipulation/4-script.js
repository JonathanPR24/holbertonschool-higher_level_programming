// 4-script.js
document.addEventListener('DOMContentLoaded', function () {
    // Select the element with id "add_item"
    var addItemElement = document.getElementById('add_item');
  
    // Select the <ul> element with class "my_list"
    var myList = document.querySelector('.my_list');
  
    // Add a click event listener to the "add_item" element
    addItemElement.addEventListener('click', function () {
      // Create a new <li> element
      var newItem = document.createElement('li');
  
      // Set the text content of the new <li> element to "Item"
      newItem.textContent = 'Item';
  
      // Append the new <li> element to the <ul> element
      myList.appendChild(newItem);
    });
  });
