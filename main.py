from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()


photo_lbl = QLabel("1234")

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

window.setLayout(main_line)
window.show()
app.exec()


app.setStyleSheet("""
        QPushButton
        {
            border-style: groove;
            border-width: 5px;
            }
        """)