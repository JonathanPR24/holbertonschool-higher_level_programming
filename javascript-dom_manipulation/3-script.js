// 3-script.js
document.addEventListener('DOMContentLoaded', function () {
    // Select the element with id "toggle_header"
    var toggleHeaderElement = document.getElementById('toggle_header');
    
    // Select the header element
    var headerElement = document.querySelector('header');
  
    // Add a click event listener to the "toggle_header" element
    toggleHeaderElement.addEventListener('click', function () {
      // Check if the header element has the class "red"
      if (headerElement.classList.contains('red')) {
        // If it has the "red" class, remove it and add the "green" class
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
      } else {
        // If it doesn't have the "red" class, remove the "green" class and add the "red" class
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
      }
    });
  });
