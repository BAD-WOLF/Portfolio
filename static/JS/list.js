const listaSuspensa = document.querySelector('.lista-suspensa');
const titulo = listaSuspensa.querySelector('.titulo');

titulo.addEventListener('click', function() {
  listaSuspensa.classList.toggle('aberto');
});
alert("test");

