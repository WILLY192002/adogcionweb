




// URL de la API
var urlApiDepartment = 'https://api-colombia.com/api/v1/Department';

// Función para obtener los departamentos al cargar la página
window.onload = function() {
  fetch(urlApiDepartment)
    .then(response => response.json())
    .then(data => {
      var selectDepartamento = document.getElementById('person_department');
      for (var i = 0; i < data.length; i++) {
        var opcion = document.createElement('option');
        opcion.value = data[i].name;
        opcion.text = data[i].name;
        opcion.setAttribute('data-id_department', data[i].id);
        selectDepartamento.add(opcion);
      }
      // Llama a cambiarCiudades para llenar las ciudades iniciales
      // changeCities();
    });
};
document.getElementById('person_department').addEventListener('change', function(e){
  var departamentoId = document.getElementById('person_department').options[document.getElementById('person_department').selectedIndex].getAttribute('data-id_department');
  fetch(urlApiDepartment + '/' + departamentoId + '/cities')
    .then(response => response.json())
    .then(data => {
      var selectCiudad = document.getElementById('person_city');
      // Limpia las opciones actuales
      selectCiudad.innerHTML = '';
      // Agrega las nuevas ciudades
      for (var i = 0; i < data.length; i++) {
        var opcion = document.createElement('option');
        opcion.value = data[i].name;
        opcion.text = data[i].name;
        selectCiudad.add(opcion);
      }
    });
})

const profile_photo = document.getElementById("preview");
const change_photo = document.getElementById("upload_photo");
var imgClickHandler = function() {
  change_photo.click();
};
profile_photo.addEventListener('click', imgClickHandler);
profile_photo.style.cursor = "pointer"

document.getElementById('upload_photo').addEventListener('change', function (e) {
  var reader = new FileReader();
  reader.onload = function (e) {
    document.getElementById('preview').src = e.target.result;
    var base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
    document.getElementById('hiddenField').value = base64String;
  }
  reader.readAsDataURL(e.target.files[0]);
});