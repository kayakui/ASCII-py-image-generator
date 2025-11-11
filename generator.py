from Demos.SystemParametersInfo import new_w
from PIL import Image
import numpy as np

# symbols = "N@#W$9876543210?!abc;:+=-,._~'"

ascii_symbols = ["N", "@", "#","W","$","9","8","7","6","5","4","3","2","1","0","?","!","a","b","c",";",":","+","=","-",",",".","_","~","'"]

def open_edit(img, new_width = 100):
    ratio = img.height / img.width / 10
    new_height = int(img.height * ratio)
    new_size = (new_width, new_height)
    resized = img.resize(new_size)
    edited_image = resized.convert("L")

    return edited_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    char = "".join([ascii_symbols[pixel//10] for pixel in pixels])

    return char

def main(new_width=100):
    path = input("type the path to image: ")
    image = Image.open(path)

    image_data = pixels_to_ascii(open_edit(image))

    pixel_count = len(image_data)
    ascii_image = "\n".join(image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # print(ascii_image)

    with open("ascii_converted2.txt", "w") as f:
        f.write(ascii_image)

main()