# Python image processing with pillow

from PIL import Image, ImageFilter

img = Image.open("LearningPython\cat_chillin.jpg")
blurred = img.filter(ImageFilter.BLUR)

rotated_img = img.rotate(180)
rotated_img.save("LearningPython\cat_chillin_rotated.jpg")

img.show()
print(img.format, img.size, img.mode)