import requests
class ImageService():
  @classmethod
  def upload_image_to_imgbb(self, image_base64):
    if image_base64 != None:
      url = "https://api.imgbb.com/1/upload"
      payload = {
          "key": '8b49247f3bbe4a7303ff983dfb758922',
          "image": image_base64
      }

      res = requests.post(url, payload)

      if res.status_code == 200:
          return res.json()
      else:
          print("Error al subir la imagen")
          return False
    else:
      return True
