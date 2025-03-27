from PIL import Image

with Image.open('Без названия.jpg')as pic_original:
    print('Зовідкритображення ')
    print('Розмір', pic_original.size)
    print('Формат', pic_original.format)
    print('Режим', pic_original.mode)
    pic_original