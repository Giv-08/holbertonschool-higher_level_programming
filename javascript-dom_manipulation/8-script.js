document.addEventListener('DOMContentLoaded', function() {
  function fetchApi() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        const greet = data;
        const hello_div = document.getElementById("hello");
        console.log(greet.hello)
        hello_div.innerHTML = `${greet.hello}`
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  };
  fetchApi();
});
