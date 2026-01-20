from PIL import Image
class ImageEditor:
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("¡Archivo no encontrado!")
        self.original.show()

MyImage = ImageEditor('Rosas.jpg')
MyImage.open()  