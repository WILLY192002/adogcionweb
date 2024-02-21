const categorias = document.getElementById("selectCategorias");
const temas = document.getElementById("selectTema");

if(categorias){
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
};




//REPORTAR PUBLICACIONES
$(document).ready(function(){
  $(".report-button").click(function(){
      var post_id = $(this).data("id");

      $.ajax({
          url: url_reportPublication,
          type: "POST",
          data: { id: post_id },
          success: function(response) {
              if(response.status === 'success') {
                alert("Gracias por tu reporte, lo revisaremos.");
              } else {
                alert("Hubo un error al reportar la publicación.");
              }
          }
      });
  });
});

