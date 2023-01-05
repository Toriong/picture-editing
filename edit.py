import fileinput
import os
import json
from PIL import Image

photoFilePath = input("Enter file path: ")

doesFileExist = os.path.exists(photoFilePath)

while not doesFileExist:
    print("ERROR! Please enter a file: ")
    photoFilePath = input("Enter file path: ")

img = None
with Image.open(photoFilePath) as img:
     img.load()

print("img.size: " + json.dumps(img.size))

width = input("Width: ")
height = input("Height: ")

while not width.isnumeric() or not height.isnumeric():
    print("ERROR! Width and height must be integers.")
    width = input("Width: ")
    height = input("Height: ")


imageOpened = Image.open(photoFilePath)
newImage = imageOpened.resize((int(width), int(height)))

newImage.save("tab_logo.png") # Or use whatever name that you want.

newImage.show()









