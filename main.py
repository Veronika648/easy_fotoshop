from PyQt6.QtWidgets import *
from PIL import Image,ImageFilter,ImageEnhance


import os

from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import *

from PIL import Image, ImageFilter, ImageEnhance


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

app = QApplication([])

app.setStyleSheet("""
        QPushButton
        {
            border-style: groove;
            border-width: 5px;
            background-color: #735fff;
            border-color: #7500ff;
            border-radius: 7px;
            color: white;
            }
            
        QWidget
        {
            background: #9e6fff;
            }
        """)
window = QWidget()


photo_lbl = QLabel("Фоточка")

photo = QListWidget()

file_btn = QPushButton("Папка")


main_line = QHBoxLayout()

v1 =QVBoxLayout()
v1.addWidget(file_btn)
v1.addWidget(photo)



left_btn = QPushButton("Вліво")
right_btn = QPushButton("Вправо")
mirror_btn = QPushButton("Дзеркало")
sharpness_btn = QPushButton("Різкість")
ch_b_btn = QPushButton("Ч/Б")

v2 =QVBoxLayout()
v2.addWidget(photo_lbl)



h1 = QHBoxLayout()
h1.addWidget(left_btn)
h1.addWidget(right_btn)
h1.addWidget(mirror_btn)
h1.addWidget(sharpness_btn)
h1.addWidget(ch_b_btn)
v2.addLayout(h1)

main_line.addLayout(v1)
main_line.addLayout(v2)

class ImageProcessor:
    def __init__ (self):
        self.folder = ""
        self.filename = ""
        self.image = ""
    def load(self):
        img_path = os.path.join(self.folder, self.filename)
        self.image = Image.open(img_path)

    def show(self):
        pix = pil2pixmap(self.image)
        pix = pix.scaledToWidth(450)
        photo_lbl.setPixmap(pix)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.show()

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.show()

    def rotate_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.show()

    def rotate_sharpness(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.show()

    def rotate_ch_b(self):
        self.image = self.image.convert("L")
        self.show()


ip = ImageProcessor()
ip.filename = "contrast.jpg"
ip.load()
ip.show()

def open_folder():
    ip.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(ip.folder)
    photo.clear()
    for file in files:
        if file.endswith(".jpg"):
            photo.addItem(file)

def show_chosen_image():
    ip.filename = photo.currentItem().text()
    ip.load()
    ip.show()

photo.currentRowChanged.connect(show_chosen_image)
file_btn.clicked.connect(open_folder)
left_btn.clicked.connect(ip.rotate_left)
right_btn.clicked.connect(ip.rotate_right)
mirror_btn.clicked.connect(ip.rotate_mirror)
sharpness_btn.clicked.connect(ip.rotate_sharpness)
ch_b_btn.clicked.connect(ip.rotate_ch_b)
window.setLayout(main_line)
window.show()
app.exec()


