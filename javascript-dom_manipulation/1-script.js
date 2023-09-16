// 1-script.js
document.addEventListener('DOMContentLoaded', function () {
    // Select the element with id "red_header"
    var redHeaderElement = document.getElementById('red_header');
  
    // Add a click event listener to it
    redHeaderElement.addEventListener('click', function () {
      // Select the header element
      var headerElement = document.querySelector('header');
  
      // Update the text color to red
      headerElement.style.color = '#FF0000';
    });
  });
