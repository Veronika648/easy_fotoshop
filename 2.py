from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('Без названия.jpg')as pic_original:
    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpg')
    pic_gray.show

with Image.open('Без названия.jpg')as pic_original:
    pic_contrast= ImageEnhance.Contrast(pic_original).enhance(1.5)
    pic_contrast.save('contrast.jpg')
    pic_contrast.show

with Image.open('Без названия.jpg')as pic_original:
    pic_filter = pic_original.filter(ImageFilter.BLUR)
    pic_filter.save('filter.jpg')
    pic_filter.show

with Image.open('Без названия.jpg')as pic_original:
    pic_corect = pic_original.filter(ImageFilter.EMBOSS )
    pic_corect.save('corect.jpg')
    pic_corect.show