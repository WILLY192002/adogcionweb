const btn_edit = document.getElementById("btn_edit");
const btn_save = document.getElementById("btn_save");
const href_edit = document.getElementById("div_edit_information");
const profile_photo = document.getElementById("preview");
const change_photo = document.getElementById("upload_photo");
const person_description = document.getElementById("person_description");
const imagenAnterior = document.getElementById("preview").src;
const title_selector = document.getElementById("title-select")
const title_selected = document.getElementById("title-selected")

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

var imgClickHandler = function() {
  change_photo.click();
};

function applyEditStyles() {
  btn_edit.textContent = "Cancelar";
  btn_edit.classList.add("btn-personalized");
  btn_save.style.display = "block";
  href_edit.style.display = "block";
  profile_photo.style.cursor = "pointer"
  title_selector.classList.remove("d-none");
  title_selected.classList.add("d-none");
  profile_photo.addEventListener('click', imgClickHandler);
  addEditStyles();
}

function resetStyles() {
  btn_edit.textContent = ""
  btn_edit.innerHTML = "<i id='icon_cog' class='bx bxs-cog'></i>";
  btn_edit.classList.remove("btn-personalized");
  btn_save.style.display = "none";
  href_edit.style.display = "none";
  change_photo.style.display = "none";
  profile_photo.style.cursor = "default"
  title_selector.classList.add("d-none");
  title_selected.classList.remove("d-none");
  profile_photo.src = imagenAnterior;
  profile_photo.removeEventListener('click', imgClickHandler);
  removeEditStyles();
}

function addEditStyles() {
  [person_description].forEach((element) => {
    element.style.background = "white";
    element.style.border = "1px solid #410002"
    element.style.cursor = "text";
    element.readOnly = false;
  });
}

function removeEditStyles() {
  [person_description].forEach((element) => {
    element.style.background = "none";
    element.style.borderStyle = "none";
    element.style.cursor = "default";
    element.readOnly = true;
  });
}



///////////////////////////////////SECCION DE PUBLICACIONES

document.getElementById('upload_photo').addEventListener('change', function(e) {
  // Crea un FileReader para leer el archivo seleccionado
  var reader = new FileReader();
  reader.onload = function(e) {
    // Cuando el archivo se ha leído, establece la imagen en la segunda ventana modal
    document.getElementById('preview').src = e.target.result;
    document.getElementById('upload_photo').style.background = "greenyellow"
    // Codifica la imagen y la guarda en oculto
    var base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
      document.getElementById('hiddenField').value = base64String;
    }
  reader.readAsDataURL(e.target.files[0]);
});


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
                $("#publication_" + post_id).fadeOut("slow", function(){
                  $(this).remove();
              });
              } else {
                  alert("Hubo un error al eliminar la publicación.");
              }
          }
      });
  });
});

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