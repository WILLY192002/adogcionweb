//----------------FUNCIONES---------------------
function validarTexto(texto) {
  if (texto.value == null || texto.value.length == 0 || /^\s+$/.test(texto.value)) {

    texto.style.border = '2px solid red';
    return false;
  } else {
    texto.style.border = '2px solid green';
    return true;
  }
}

function checkPassword(valor) {
  var myregex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
  if (myregex.test(valor)) {
    return true;
  } else {
    return false;
  }
}

function validarNumero(limInf, limSup, numero) {
  if (limInf <= (numero.value).length && (numero.value).length <= limSup) {
    numero.style.border = '2px solid green';
    return true;
  } else {
    numero.style.border = '2px solid red';
    return false;
  }
}


//----------------FIN FUNCIONES ----------------


//############### ESTETICA BARRA PROGRESO############
const numProgreso = document.querySelectorAll(".num");
let max = 3;
let cont = 1;

//###############FIN ESTETICA BARRA PROGRESO############

// ###############MOSTRAR CONTRASEÑA###################

var campo1 = document.getElementById("contrasenaAlb")
var campo2 = document.getElementById("contraConf")
var checkBox = document.getElementById("flexCheckDefault")

checkBox.addEventListener('change', function () {
  if (checkBox.checked) {
    campo1.type = "text";
    campo2.type = "text";
  } else {
    campo1.type = "password";
    campo2.type = "password";
  }
});

//############FIN MOSTRAR CONTRESEÑA#################

//############ MOVIMIENTO PAGINA#####################
//PAGINA 1
const movPag1 = document.querySelector(".pag1");
const btn_adelante2 = document.querySelector(".sigPag2");

btn_adelante2.addEventListener('click', function (e) {
  e.preventDefault();

  var nombre1 = document.getElementById("nombre1");
  var apellido1 = document.getElementById("apellido1");
  var numeroDoc = document.getElementById("numeroDoc");
  if (validarTexto(nombre1) && validarTexto(apellido1) && validarNumero(8, 10, numeroDoc)) {
    movPag1.style.marginLeft = "-33%";
    numProgreso[cont - 1].classList.add("activate");
    cont += 1;
  } else {
    alert("Verifique que los campos en ROJO");
  }
})

// //PAGINA 2
// const btn_adelante3 = document.querySelector(".sigPag3");
// const btn_atras1 = document.querySelector(".antPag1");

// btn_adelante3.addEventListener('click', function (e) {
//   e.preventDefault();
//   var nombreAlb = document.getElementById("nombreAlb");
//   if (validarTexto(nombreAlb) ) {
//     movPag1.style.marginLeft = "-66%";
//     numProgreso[cont - 1].classList.add("activate");
//     cont += 1;
//   } else {
//     alert("Verifique que los campos en ROJO");
//   }

// })

// btn_atras1.addEventListener('click', function (e) {
//   e.preventDefault();
//   movPag1.style.marginLeft = "0%"
//   numProgreso[cont - 2].classList.remove("activate");
//   cont -= 1;
// })

//PAGINA 3
const btn_fin = document.querySelector(".finalizar");
const btn_atras2 = document.querySelector(".antPag2");

btn_fin.addEventListener('click', function (e) {
  //e.preventDefault();
  var correo = document.getElementById("CorreoAlb")
  var correoConf = document.getElementById("correoConf")
  var contrasena = document.getElementById("contrasenaAlb")
  var contraConf = document.getElementById("contraConf")
  var formulario = document.getElementById("formRegister")
  if (1 == 1) {
    if (checkPassword(contrasena.value) && (contrasena.value == contraConf.value)) {
      numProgreso[cont - 2].classList.add("activate");
      cont += 1;
      alert("El cuestionario ha finalizado");
      formulario.submit();
    } else {
      e.preventDefault();
      alert("La contrasena es insegura");
    }
  } else {
    e.preventDefault();
    alert("Los correos no coinciden");
  }


})

btn_atras2.addEventListener('click', function (e) {
  e.preventDefault();
  movPag1.style.marginLeft = "0%"
  numProgreso[cont - 2].classList.remove("activate");
  cont -= 1;
})
//############FIN MOVIMIENTO PAGINA#####################




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