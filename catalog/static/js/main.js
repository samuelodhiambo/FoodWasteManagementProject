const element = document.getElementById('content');
const modal = document.getElementById('productModal');
const menu = document.getElementById("menu");
function showDropdown() {
    element.classList.toggle('show');
}

function showModal(x) {
    const productName = document.getElementById('productName');
    const productImage = document.getElementById("productImage");

    productName.innerText = x.name;

    productImage.setAttribute("src", x.image);

    modal.classList.toggle('show')

}

function closeModal() {
    modal.classList.add('show')
}
function showMenu() {

    menu.classList.toggle("hidden");

}

