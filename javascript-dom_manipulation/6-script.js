// 6-script.js
document.addEventListener('DOMContentLoaded', function () {
    // Select the element with id "character"
    var characterElement = document.getElementById('character');
  
    // Define the URL of the API
    var apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  
    // Fetch data from the API
    fetch(apiUrl)
      .then(function (response) {
        // Check if the response is successful (status code 200)
        if (response.status === 200) {
          // Parse the JSON response
          return response.json();
        } else {
          // Handle the error
          throw new Error('Failed to fetch data');
        }
      })
      .then(function (data) {
        // Extract the character name from the data
        var characterName = data.name;
  
        // Display the character name in the "character" element
        characterElement.textContent = characterName;
      })
      .catch(function (error) {
        // Handle any errors that occurred during the fetch
        console.error(error);
      });
  });
