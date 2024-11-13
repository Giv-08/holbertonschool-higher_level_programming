function fetchApi() {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const movies = data // results is an array
      movies.results.forEach(movie => {
        const list_movies = document.getElementById('list_movies');
        const li = document.createElement('li');

        li.innerHTML = `${movie.title}`;
        list_movies.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
};
window.onload = fetchApi();
