function fetchApi() {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const characters = data
      const character_div = document.getElementById('character');
      character_div.innerHTML = `${characters.name}`;
      })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
};
window.onload = fetchApi();
