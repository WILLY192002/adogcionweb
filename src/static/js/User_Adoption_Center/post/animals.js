// Escucha el evento 'change' del input del archivo
document.getElementById('foto').addEventListener('change', function(e) {
    // Crea un FileReader para leer el archivo seleccionado
    var reader = new FileReader();
    reader.onload = function(e) {
      // Cuando el archivo se ha leído, establece la imagen en la segunda ventana modal
      document.getElementById('preview').src = e.target.result;
      // Muestra la segunda ventana modal
      var myModal = new bootstrap.Modal(document.getElementById('Modal2'));
      myModal.show();
      // Codifica la imagen y la guarda en oculto
      var base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
        document.getElementById('hiddenField').value = base64String;
      }
    reader.readAsDataURL(e.target.files[0]);
});

$('#Modal, #Modal2').on('hidden.bs.modal', function (e) {
  // Restablece todos los inputs de tipo 'text' y 'file'
  $(this).find('input[type="text"], input[type="file"]').val('');
  // Restablece todas las áreas de texto
  $(this).find('textarea').val('');
  // Restablece la imagen de vista previa
  document.getElementById('preview').src = '';

  // Verifica si la otra ventana modal está abierta
  if ($('#Modal').is(':visible')) {
    // Si la ventana modal 'Modal' está abierta, ciérrala
    var myModal = bootstrap.Modal.getInstance(document.getElementById('Modal'));
    myModal.hide();
  } else if ($('#Modal2').is(':visible')) {
    // Si la ventana modal 'Modal2' está abierta, ciérrala
    var myModal2 = bootstrap.Modal.getInstance(document.getElementById('Modal2'));
    myModal2.hide();
  }
})

function checkEspecie() {
  var especie = document.getElementById('especieSelect').value;
  var tamanio = document.getElementById('tamanioSelect');

  Array.from(tamanio.options).forEach(option => {
    if ((especie == 'Conejo' || especie == 'Hamster') && option.value != 'Pequeño'){
      option.style.display =  "none";
    }else{
      option.style.display =  "block";
    }

    // const temasSeleccionado = option.classList.contains(categoriaSeleccionada);
    // option.style.display = temasSeleccionado ? "block" : "none";
  });
  
  // if (especie == 'Conejo' || especie == 'Hamster') {
  //   tamanio.disabled = true;
  // } else {
  //   tamanio.disabled = false;
  // }
}

//Capturar información para "abrir"
$(document).ready(function() {
  $('[id^="open-btn-"]').click(function() {
    // Llena los campos del formulario con los datos del animal
    $('#idAnimal').val($(this).data('idanimal'))
    $('#fotografia').attr('src', $(this).data('fotografia'));
    $('#nombre').val($(this).data('nombre'));
    $('#edad').val($(this).data('edad'));
    $('#especie').val($(this).data('especie'));
    $('#sexo').val($(this).data('sexo'));
    $('#raza').val($(this).data('raza'));
    $('#tamanio').val($(this).data('tamanio'));
    $('#pesoEdit').val($(this).data('peso'));
    $('#estado_medico').val($(this).data('estado_medico'));
  });
});

//Mostrar filtro
document.getElementById('botonFiltrar').addEventListener('click', function() {
  var divFiltro = document.getElementById('filter_animal_div');
  console.log("hola");
  if (divFiltro.style.display === 'none') {
    divFiltro.style.display = 'block';
  } else {
    divFiltro.style.display = 'none';
  }
});


