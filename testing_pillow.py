from PIL import Image

filename = "Doraemon.jpg"

img = Image.open(filename)

pixel_data = img.load()

list_of_pixels = list(img.getdata())

for x in range(100):
    for y in range(100):
        pixel_data[x, y] = (255, 255, 255)

img.show()
print(list_of_pixels)
