function toggleColor() {
  header = document.querySelector('header');
  toggle_header = document.getElementById('toggle_header');

  if (header.classList.contains("green")) {
    header.classList.remove("green");
    header.classList.add("red");
  } else {
    header.classList.remove("red");
    header.classList.add("green");
  }
};
