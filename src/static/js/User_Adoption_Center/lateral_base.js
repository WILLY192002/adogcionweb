// Selecciona el formulario y el botón por sus ID
var form = document.querySelector('#createPublication');
var btn = document.querySelector('#nextButton');

// Añade un evento 'input' al formulario
form.addEventListener('input', function() {
  // Selecciona todos los campos requeridos
  var primerNombre = document.querySelector('input[name="primerNombre"]');
  var primerApellido = document.querySelector('input[name="primerApellido"]');
  var tipoDocumento = document.querySelector('select[name="tipoDocumento"]');
  var numeroDocumento = document.querySelector('input[name="numeroDocumento"]');

  // Comprueba si todos los campos requeridos están llenos
  if (primerNombre.value && primerApellido.value && tipoDocumento.value && numeroDocumento.value !== "") {
    // Habilita el botón si todos los campos requeridos están llenos
    btn.disabled = false;
  } else {
    // Deshabilita el botón si no todos los campos requeridos están llenos
    btn.disabled = true;
  }
});

// Deshabilita el botón al cargar la página
window.onload = function() {
  btn.disabled = true;
}

//---------------------------------------------------------------------------------------------
$('#ModalCreate').on('hidden.bs.modal', function (e) {
  // Restablece todos los inputs de tipo 'text' y 'file'
  $(this).find('input[type="text"], input[type="number"], input[type="file"], select, textarea').val('');
  // Restablece todas las áreas de texto
  $(this).find('textarea').val('');

  // Verifica si la otra ventana modal está abierta
  if ($('#ModalRequest').is(':visible')) {
    // Si la ventana modal 'Modal' está abierta, ciérrala
    var ModalRequest = bootstrap.Modal.getInstance(document.getElementById('ModalRequest'));
    ModalRequest.hide();
  }
});


//--------------------------------------------------------------------------------------------
// Selecciona el botón personalizado y el elemento de entrada
var uploadButton = document.querySelector('#uploadButton');
var fileInput = document.querySelector('#fileInput');

// Añade un evento 'click' al botón personalizado
uploadButton.addEventListener('click', function() {
  // Activa el elemento de entrada oculto
  fileInput.click();
});
//Codificar la imagen
document.getElementById('fileInput').addEventListener('change', function(e) {
  if (e.target.files.length > 0) {
    // Si se seleccionó un archivo, lo leemos como URL de datos
    var reader = new FileReader();
    reader.onload = function(e) {
      // Cuando el archivo se ha leído, puedes codificar la imagen y guardarla en un campo oculto
      var base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
      document.getElementById('hiddenFile').value = base64String;
    }
    reader.readAsDataURL(e.target.files[0]);
  }
});


//--------------------------------------------------------------------------------------------
var textPublicacion = document.querySelector('#textPublicacion');
var fileInput = document.querySelector('#fileInput');
var submitButton = document.querySelector('#submitButton');

// Añade un evento 'input' al textarea
textPublicacion.addEventListener('input', function() {
  // Habilita el botón "Publicar" si el textarea tiene contenido o si se ha seleccionado un archivo
  submitButton.disabled = !(textPublicacion.value || fileInput.files.length > 0);
});

// Añade un evento 'change' al input del archivo
fileInput.addEventListener('change', function() {
  // Habilita el botón "Publicar" si se ha seleccionado un archivo o si el textarea tiene contenido
  submitButton.disabled = !(fileInput.files.length > 0 || textPublicacion.value);
});
