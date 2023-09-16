// 5-script.js
document.addEventListener('DOMContentLoaded', function () {
    // Select the element with id "update_header"
    var updateHeaderElement = document.getElementById('update_header');
  
    // Select the header element
    var headerElement = document.querySelector('header');
  
    // Add a click event listener to the "update_header" element
    updateHeaderElement.addEventListener('click', function () {
      // Update the text content of the header element
      headerElement.textContent = 'New Header!!!';
    });
  });
