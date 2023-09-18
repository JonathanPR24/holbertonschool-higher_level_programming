var list_movies = document.getElementById('list_movies')

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
.then(function(response){
    if (!response.ok){
        throw new Error("Error on Network response")
    }
    return response.json();
})
.then(function(data){
    console.log(data)
    data.results.forEach(function(movie){
        var movie_title = document.createElement('li');

        movie_title.textContent = movie.title;

        list_movies.appendChild(movie_title);
    });
})
.catch(function(error){
    console.error("There was a problem with the fetch operation:", error);
});
