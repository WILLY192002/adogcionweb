const categorias = document.getElementById("selectCategorias");
const temas = document.getElementById("selectTema");

categorias.addEventListener("change", function (e) {
  const categoriaSeleccionada = categorias.value;
  temas.disabled = false
  if (categoriaSeleccionada) {
    var x = ""
    Array.from(temas.options).forEach(option => {
      x = x + option.classList 
      const temasSeleccionado = option.classList.contains(categoriaSeleccionada);
      option.style.display = temasSeleccionado ? "block" : "none";
    });
  }
})

