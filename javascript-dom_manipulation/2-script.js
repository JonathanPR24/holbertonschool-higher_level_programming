// 2-script.js
document.addEventListener('DOMContentLoaded', function () {
    // Select the element with id "red_header"
    var redHeaderElement = document.getElementById('red_header');
  
    // Add a click event listener to it
    redHeaderElement.addEventListener('click', function () {
      // Select the header element
      var headerElement = document.querySelector('header');
  
      // Add the class "red" to the header element
      headerElement.classList.add('red');
    });
  });
