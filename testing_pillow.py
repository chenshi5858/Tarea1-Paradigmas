from PIL import Image

filename = "Doraemon.jpg"

img = Image.open(filename)

print(img)

pixel_data = img.load()

print(img.size)

#list_of_pixels = list(img.getdata())

for x in range(100):
    for y in range(100):
        pixel_data[x, y] = (255, 255, 255)

img.show()
#Image.open(filename).show()
#print(list_of_pixels)
