// 7-script.js
document.addEventListener('DOMContentLoaded', function () {
    // Select the ul element with id "list_movies"
    var listMoviesElement = document.getElementById('list_movies');
  
    // Define the URL of the API
    var apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
  
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
        // Extract the list of movies from the data
        var movies = data.results;
  
        // Loop through the movies and add their titles to the list
        movies.forEach(function (movie) {
          var listItem = document.createElement('li');
          listItem.textContent = movie.title;
          listMoviesElement.appendChild(listItem);
        });
      })
      .catch(function (error) {
        // Handle any errors that occurred during the fetch
        console.error(error);
      });
  });
