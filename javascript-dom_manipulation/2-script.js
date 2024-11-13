function changeColor() {
  header = document.querySelector('header');
  red_header = document.getElementById('red_header');

  red_header.addEventListener("click", function () {
      header.classList.add("red");
    });
};
