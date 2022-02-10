const element = document.getElementById('content');
const modal = document.getElementById('productModal');
const menu = document.getElementById("menu");
function showDropdown() {
    element.classList.toggle('show');
}

function showModal() {
    modal.classList.toggle('show')
}

function closeModal() {
    modal.classList.add('show')
}
function showMenu() {

    menu.classList.toggle("show");

}