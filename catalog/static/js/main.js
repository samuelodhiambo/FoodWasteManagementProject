const element = document.getElementById('content');
const modal = document.getElementById('productModal');
function showDropdown() {
    element.classList.toggle('show');
}

function showModal() {
    modal.classList.toggle('show')
}

function closeModal() {
    modal.classList.add('show')
}
