from PIL import Image

img = Image.open('shot2.png')
img.show()


# r_pixels = list(img.getdata(0))
# g_pixels = list(img.getdata(1))
pixels = list(img.getdata(1))
# b_pixels = list(img.getdata(2))
# width, height = img.size
# pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
# print(pixels)

