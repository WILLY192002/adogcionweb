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


////////////////////////Operations, diseases, vaccine
function updateSelection(select_id, Container_id, type) {
  var selectElement = document.getElementById(select_id);
  var selectedValue = selectElement.value;
  var selectedText = selectElement.options[selectElement.selectedIndex].text;
  // Verificar si ya existe un label para evitar duplicados
  if (document.getElementById(type+"_"+selectedValue)) {
    var temporal = document.getElementById('div_'+type+'_'+selectedValue)
    if (temporal.style.display == 'none'){
      temporal.style.display = 'block';
      document.getElementById(type+"_"+selectedValue).name = type+"_"+selectedValue;
    }else{
      alert('Ya está registrada');
    }
    
    return;
  }

  // Crear un div que tendrá cada opcion
  var divElement = document.createElement("div");
  divElement.classList.add("option_added");
  divElement.id = 'div_'+type+"_"+selectedValue;

  // Crear un label con el texto de la opción seleccionada
  var idlabelElement = document.createElement("input");
  idlabelElement.value = selectedValue;
  idlabelElement.type = "hidden";
  idlabelElement.name = type+"_id";
  idlabelElement.id = type+"_"+selectedValue;

  // Crear un label con el texto de la opción seleccionada
  var labelElement = document.createElement("label");
  labelElement.textContent = selectedText;

  // Crear un botón para eliminar la opción seleccionada
  var removeButton = document.createElement("button");
  removeButton.textContent = "Quitar";
  removeButton.onclick = function() {
      // Eliminar el label y el botón al hacer clic
      divElement.remove();
      // idlabelElement.remove();
      // labelElement.remove();
      // removeButton.remove();
      // Restaurar el valor predeterminado en el select
      selectElement.value = "";
  };

  divElement.appendChild(idlabelElement);
  divElement.appendChild(labelElement);
  divElement.appendChild(removeButton);

  // Agregar el label y el botón al contenedor
  var container = document.getElementById(Container_id);
  container.appendChild(divElement);
  
}


//////////delete operations, diseases, vaccines
function changeName(input_id, div_id, type,event) {
  event.preventDefault();
  var inputSelected = document.getElementById(input_id)
  inputSelected.name = 'deleted_'+type

  var divSelected = document.getElementById(div_id)
  divSelected.style.display = 'none'

}


