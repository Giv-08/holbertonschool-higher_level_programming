function addItems() {
  const ul = document.querySelector('.my_list');
  const newItem = document.createElement("li");

  newItem.textContent = "Item";
  ul.appendChild(newItem);
}
