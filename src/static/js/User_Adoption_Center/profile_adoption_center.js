
const btn_editar = document.getElementById("btn_edit");
const btn_guardar = document.getElementById("btn_guardar");
const nombreAlb = document.getElementById("nombreAlb");
const descripAlb = document.getElementById("descripAlb");
const departAlb = document.getElementById("departAlb");
const contactoAlb = document.getElementById("contactoAlb");
const direccionAlb = document.getElementById("direccionAlb");
const ciudadAlb = document.getElementById("ciudadAlb");
// const MediosAyuda = document.getElementById("MediosAyuda");
const cambiarFoto = document.getElementById("subirFoto");
const fotoPerfil = document.getElementById("preview");

const imagenAnterior = document.getElementById("preview").src;
const edit_Full = document.getElementById("href_editP")


let changed = false;

function toggleStyles(e) {
  e.preventDefault();
  if (changed) {
    resetStyles();
  } else {
    applyEditStyles();
  }
  e.preventDefault();
  changed = !changed;
}

// btn_editar.addEventListener('click', function (e) {
//   e.preventDefault();

//   if (changed) {
//     resetStyles();
//   } else {
//     applyEditStyles();
//   }
//   changed = !changed;
// });
//Seleccionar foto 
var imgClickHandler = function() {
  cambiarFoto.click();
};

function applyEditStyles() {
  btn_editar.textContent = "Cancelar";
  btn_editar.classList.add("btn-personalized");
  btn_guardar.style.display = "block";
  edit_Full.style.display = "block";
  fotoPerfil.style.cursor = "pointer"
  fotoPerfil.addEventListener('click', imgClickHandler);
  addEditStyles();
}

function resetStyles() {
  btn_editar.textContent = ""
  btn_editar.innerHTML = "<i id='icon_cog' class='bx bxs-cog'></i>";
  btn_editar.classList.remove("btn-personalized");
  btn_guardar.style.display = "none";
  cambiarFoto.style.display = "none";
  edit_Full.style.display = "none";
  fotoPerfil.style.cursor = "default"
  fotoPerfil.src = imagenAnterior;
  fotoPerfil.removeEventListener('click', imgClickHandler);
  removeEditStyles();
}

function addEditStyles() {
  [nombreAlb, descripAlb, departAlb, contactoAlb, ciudadAlb].forEach((element) => {
    element.style.background = "white";
    element.style.border = "1px solid #410002"
    element.style.cursor = "text";
    element.readOnly = false;
  });
}

function removeEditStyles() {
  [nombreAlb, descripAlb, departAlb, contactoAlb, ciudadAlb].forEach((element) => {
    element.style.background = "none";
    element.style.borderStyle = "none";
    element.style.cursor = "default";
    element.readOnly = true;
  });
}

///////////////////////////////////SECCION DE PUBLICACIONES

document.getElementById('subirFoto').addEventListener('change', function(e) {
  // Crea un FileReader para leer el archivo seleccionado
  var reader = new FileReader();
  reader.onload = function(e) {
    // Cuando el archivo se ha leído, establece la imagen en la segunda ventana modal
    document.getElementById('preview').src = e.target.result;
    document.getElementById('subirFoto').style.background = "greenyellow"
    // Codifica la imagen y la guarda en oculto
    var base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
      document.getElementById('hiddenField').value = base64String;
    }
  reader.readAsDataURL(e.target.files[0]);
});


///////MOSTRAR FILTRO EN ADOPTAR

//Mostrar filtro
var botonFiltrar = document.getElementById('botonFiltrar');

if (botonFiltrar) {
  document.getElementById('botonFiltrar').addEventListener('click', function() {
    var divFiltro = document.getElementById('filter_animal_div');
    console.log("hola");
    if (divFiltro.style.display === 'none') {
      divFiltro.style.display = 'block';
    } else {
      divFiltro.style.display = 'none';
    }
  });
}



//////MOSTRAR BOTON ADOPTAR

// Obtén todos los elementos con la clase "publicacion"
var publicaciones = document.getElementsByClassName('publicacion');

// Recorre cada elemento
for (var i = 0; i < publicaciones.length; i++) {
  // Añade el evento de "mouseover"
  publicaciones[i].addEventListener('mouseover', function() {
    // Encuentra el div "cont-btn-adoptar" dentro de este elemento
    var btnAdoptar = this.getElementsByClassName('btn-adoptar')[0];
    // Asigna la clase "mostrar" al div "cont-btn-adoptar"
    btnAdoptar.className = 'btn-adoptar btn-adoptar-mostrar';
  });

  // Añade el evento de "mouseout"
  publicaciones[i].addEventListener('mouseout', function() {
    // Encuentra el div "cont-btn-adoptar" dentro de este elemento
    var btnAdoptar = this.getElementsByClassName('btn-adoptar')[0];
    // Asigna la clase "ocultar" al div "cont-btn-adoptar"
    btnAdoptar.className = 'btn-adoptar btn-adoptar-ocultar';
  });
}



//ELIMINAR PUBLICACIONES
$(document).ready(function(){
  $(".delete-button").click(function(){
      var post_id = $(this).data("id");

      $.ajax({
          url: url_delete_publication,
          type: "POST",
          data: { id: post_id },
          success: function(response) {
              if(response.status === 'success') {
                $("#publicacion_" + post_id).fadeOut("slow", function(){
                  $(this).remove();
              });
              } else {
                  alert("Hubo un error al eliminar la publicación.");
              }
          }
      });
  });
});


