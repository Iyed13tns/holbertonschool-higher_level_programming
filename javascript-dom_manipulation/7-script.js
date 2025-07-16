// Fetch the data from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        
        const movies = data.results;
        const listMovies = document.getElementById('list_movies');

        movies.forEach(movie => {
            const listItem = document.createElement('li');
            listItem.textContent = movie.title;
            listMovies.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });