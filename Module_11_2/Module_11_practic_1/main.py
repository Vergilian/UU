from PIL import Image
from PIL import ImageDraw, ImageFont


# im = Image.open('photo.jpg')
#
# print(im.format, im.size, im.mode)
# w, h = im.size
#
# out = im.resize((w//2, h//2))
# out.show()

def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))


im = new_photo('photo.jpg')
im_2 = new_photo('sun.png')


w, h = im.size

im.paste(im_2, (w-800, h-280))

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('ofont.ru_Rammetto One.ttf', 30)
draw.text((100, 200), 'Привет, дорогой друг', font=font, fill='yellow')

im.show('MyPhoto')
