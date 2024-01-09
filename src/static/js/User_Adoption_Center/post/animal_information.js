const cambiarFoto = document.getElementById("subirFoto");
const fotoPerfil = document.getElementById("preview");

const imagenAnterior = document.getElementById("preview").src;

var imgClickHandler = function () {
  cambiarFoto.click();
};

fotoPerfil.addEventListener('click', imgClickHandler);
fotoPerfil.style.cursor = "pointer"

document.getElementById('subirFoto').addEventListener('change', function (e) {
  // Crea un FileReader para leer el archivo seleccionado
  var reader = new FileReader();
  reader.onload = function (e) {
    // Cuando el archivo se ha leído, establece la imagen en la segunda ventana modal
    document.getElementById('preview').src = e.target.result;
    document.getElementById('subirFoto').style.background = "greenyellow"
    // Codifica la imagen y la guarda en oculto
    var base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
    document.getElementById('hiddenField').value = base64String;
  }
  reader.readAsDataURL(e.target.files[0]);
});




////////////////////////


const species = document.getElementById("animal_specie");
const breed = document.getElementById("animal_breed");

species.addEventListener("change", function (e) {
  const specieseleccionada = species.value;
  breed.disabled = false
  if (specieseleccionada) {
    var x = ""
    Array.from(breed.options).forEach(option => {
      x = x + option.classList 
      const breedSeleccionado = option.classList.contains(specieseleccionada);
      option.style.display = breedSeleccionado ? "block" : "none";
    });
  }
})