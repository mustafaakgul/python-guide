from PIL import Image

img = Image.open("images/lena.png")
img.show()
print(img.size)