from PIL import Image

class Open_image:
    def __init__(self, img_path):
        self.img_path = img_path
        self.pixel_list = []
    
    def open_img(self):
        return Image.open(self.img_path)
    
    def load_img(self):
        return self.open_img().load()
    
    def get_pixels(self):
        self.pixel_list = list(self.open_img().getdata())

class Negative_filter(Open_image):
    def __init__(self, img_path):
        super().__init__(img_path)
        self.negative_pixel_list = []

    def pixels_to_negative(self):
        for pixel in self.pixel_list:
            pixel=list(pixel)
            pixel = [abs(i-255) for i in pixel]
            self.negative_pixel_list.append(tuple(pixel))

    def transform_image_to_negative(self):
        width, height = self.open_img().size
        counter = 0
        for x in range(width):
            for y in range(height):
                self.load_img()[x, y] = self.negative_pixel_list[counter]
                counter += 1
        self.open_img().show()
        self.open_img().save("negative_image.jpg")

        

Doraemon = Negative_filter("Doraemon.jpg")
Doraemon.get_pixels()
Doraemon.pixels_to_negative()
Doraemon.transform_image_to_negative()

