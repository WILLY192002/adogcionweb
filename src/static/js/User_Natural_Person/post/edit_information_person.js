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
        opcion.value = data[i].id;
        opcion.text = data[i].name;
        selectDepartamento.add(opcion);
      }
      // Llama a cambiarCiudades para llenar las ciudades iniciales
      changeCities();
    });
};

// Función para cambiar las ciudades cuando se selecciona un nuevo departamento
function changeCities() {
  var departamentoId = document.getElementById('person_department').value;
  fetch(urlApiDepartment + '/' + departamentoId + '/cities')
    .then(response => response.json())
    .then(data => {
      var selectCiudad = document.getElementById('person_city');
      // Limpia las opciones actuales
      selectCiudad.innerHTML = '';
      // Agrega las nuevas ciudades
      for (var i = 0; i < data.length; i++) {
        var opcion = document.createElement('option');
        opcion.value = data[i].id;
        opcion.text = data[i].name;
        selectCiudad.add(opcion);
      }
    });
}
