/*const cambiarFoto = document.getElementById("foto");

var imgClickHandler = function () {
  cambiarFoto.click();
};

fotoPerfil.addEventListener('click', imgClickHandler);
fotoPerfil.style.cursor = "pointer"*/

document.getElementById('foto_subida').addEventListener('change', function (e) {
  var reader = new FileReader();
  reader.onload = function (e) {
      document.getElementById('preview').src = e.target.result;
      document.getElementById('preview').style.display = 'block';
      var base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
      document.getElementById('hiddenField').value = base64String;
  }
  reader.readAsDataURL(e.target.files[0]);
});

