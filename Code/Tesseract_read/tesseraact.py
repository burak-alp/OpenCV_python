from PIL import Image
import pytesseract

img=Image.open("D:\\OpenCV\\test_images\\text.png")
text=pytesseract.image_to_string(img,lang="eng")
print(text)