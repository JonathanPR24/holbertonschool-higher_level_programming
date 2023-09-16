// 8-script.js
document.addEventListener('DOMContentLoaded', function () {
    // Select the element with id  "hello"
    var helloElement = document.getElementById('hello');
  
    // Define the URL for fetching the translation
    var apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
    // Fetch the translation from the API
    fetch(apiUrl)
      .then(function (response) {
        // Check if the response is successful (status code 200)
        if (response.status === 200) {
          // Parse the response as JSON
          return response.json();
        } else {
          // Handle the error
          throw new Error('Failed to fetch translation');
        }
      })
      .then(function (data) {
        // Extract the translation from the data
        var translation = data.hello;
  
        // Display the translation in the "hello" element
        helloElement.textContent = translation;
      })
      .catch(function (error) {
        // Handle any errors that occurred during the fetch
        console.error(error);
      });
  });
