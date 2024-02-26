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


///////////////////////////////EDITAR NUMEROS

/////MANEJAR LOS REGISTRADOS
var checkboxesRegistrados = document.querySelectorAll('.check-input-mdr');

checkboxesRegistrados.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    // Obtener el campo de entrada asociado mediante el atributo data-target
    if(this.getAttribute('data-target') != null){
      var targetId = this.getAttribute('data-target');
      var input = document.getElementById(targetId);
      input.disabled = !this.checked;
    }
    
  });
});

//////// MANEJAR LOS NO REGISTRADOS
var checkboxesNoRegistrados = document.querySelectorAll('.check-input-mdNr');
checkboxesNoRegistrados.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    // Obtener el campo de entrada asociado mediante el atributo data-target
    var targetId = this.getAttribute('data-target');
    var input = document.getElementById(targetId);
    input.disabled = !this.checked;
    if (!this.checked) {
      input.value = "Ingrese el numero";
    } else {
      input.value = "";
    }
  });
});

///////////////////LINK DE GOOGLE MAPS
check_generar_link = document.getElementById('flexSwitchCheckDefault');
label_link_generado = document.getElementById('label-link-generado')

tipo_via = document.getElementById('selectTipoVia')
numero_via = document.getElementById('numero-via')
complemento_via = document.getElementById('complemento-via')
InicioCuadra = document.getElementById('cuadraInicio')
finCuadra= document.getElementById('cuadraFin')
linkreferencia= document.getElementById('ref-link-generado')

departamento = document.getElementById('person_department')
ciudad = document.getElementById('person_city')

contenedor_generar_link = document.getElementById('sec-link-google-maps')
contenedor_alt_link = document.getElementById('sec-alt-link')






////CAMPOS DE DIRECCION
check_cambiar_direccion = document.getElementById('checkCambiarDireccion')
contenedor_form_ubicacion = document.getElementById('form-direccion')
input_link_ubicacion = document.getElementById('input_link_ubicacion')


check_cambiar_direccion.addEventListener('change', function(){
  if(check_cambiar_direccion.checked){
    contenedor_form_ubicacion.style.display = "block"
  }else{
    contenedor_form_ubicacion.style.display = "none"
  }
})



///MOSTRAR SECCION DE LINK
check_generar_link.addEventListener('change', function () {
  if(check_generar_link.checked){
    link = tipo_via.value+"+"+numero_via.value;
    if (complemento_via.value != ''){
      link += "+"+complemento_via.value;
    }

    if(InicioCuadra.value != '' && finCuadra.value != ''){
      link += "%23"+InicioCuadra.value+"-"+finCuadra.value
    }
    
    link += ","
    
    alert(departamento.value)
    linkreferencia.textContent = "https://www.google.com/maps/search/?api=1&query="+link
    linkreferencia.href = "https://www.google.com/maps/search/?api=1&query="+link+"+"+ciudad.value+",+"+departamento.value
    input_link_ubicacion.value = "https://www.google.com/maps/search/?api=1&query="+link+"+"+ciudad.value+",+"+departamento.value
    contenedor_generar_link.style.display = "block"
    contenedor_alt_link.style.display = "block"
  }else{
    contenedor_generar_link.style.display = "none"
    contenedor_alt_link.style.display = "none"
  }
});



// CONSUMO API PARA DEPARTAMENTOS

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

// Función para cambiar las ciudades cuando se selecciona un nuevo departamento
function changeCities() {
  var departamentoId = document.getElementById('person_department').options[document.getElementById('person_department').selectedIndex].getAttribute('data-id_department');
  // var departamentoId = document.getElementById('person_department').value;
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
}