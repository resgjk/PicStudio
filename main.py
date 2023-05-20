import sys

from PIL import Image, ImageFilter
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QPushButton



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('PicStudioUI.ui', self)

        self.setWindowIcon(QIcon('PicStudioIcon.png'))

        self.degree = 0
        self.pic_tr = False
        self.chb_tr = False
        self.negative_tr = False
        self.light_tr = False
        self.blur_tr = False
        self.contour_tr = False
        self.detail_tr = False
        self.edge_enhance_tr = False
        self.eem_tr = False
        self.emboss_tr = False
        self.find_edges_tr = False
        self.smooth_tr = False
        self.sharpen_tr = False
        self.red_tr = False
        self.green_tr = False
        self.blue_tr = False
        self.stereopara_tr = False
        self.white_tr = False
        self.black_tr = False
        self.pc_cp = ''

        self.red_slider.setMinimum(0)
        self.red_slider.setMaximum(255)
        self.red_slider.setValue(0)

        self.green_slider.setMinimum(0)
        self.green_slider.setMaximum(255)
        self.green_slider.setValue(0)

        self.blue_slider.setMinimum(0)
        self.blue_slider.setMaximum(255)
        self.blue_slider.setValue(0)

        self.rotation_slider.setMinimum(-360)
        self.rotation_slider.setMaximum(360)
        self.rotation_slider.setValue(0)

        self.one_page_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.two_page_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.three_page_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.four_page_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.five_page_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.open_button.clicked.connect(self.open)
        self.left_90_button.clicked.connect(self.rotation_left)
        self.left_180_button.clicked.connect(self.rotation_left)
        self.left_270_button.clicked.connect(self.rotation_left)
        self.right_90_button.clicked.connect(self.rotation_right)
        self.right_180_button.clicked.connect(self.rotation_right)
        self.right_270_button.clicked.connect(self.rotation_right)
        self.horizont_button.clicked.connect(self.mirror_horizont)
        self.vertical_button.clicked.connect(self.mirror_vertical)
        self.red_slider.valueChanged.connect(self.red_change)
        self.green_slider.valueChanged.connect(self.green_change)
        self.blue_slider.valueChanged.connect(self.blue_change)
        self.all_button.clicked.connect(self.all)
        self.delete_button.clicked.connect(self.delete)
        self.chb_button.clicked.connect(self.chb)
        self.negative_button.clicked.connect(self.negative)
        self.light_button.clicked.connect(self.light)
        self.blur_button.clicked.connect(self.blur)
        self.contour_button.clicked.connect(self.contour)
        self.detail_button.clicked.connect(self.detail)
        self.edge_enhance_button.clicked.connect(self.edge_enhance)
        self.eem_button.clicked.connect(self.eem)
        self.emboss_button.clicked.connect(self.emboss)
        self.find_edges_button.clicked.connect(self.find_edges)
        self.smooth_button.clicked.connect(self.smooth)
        self.sharpen_button.clicked.connect(self.sharpen)
        self.save_as_button.clicked.connect(self.save_as)
        self.rotation_slider.valueChanged.connect(self.rotation_slide)
        self.red_button.clicked.connect(self.red_func)
        self.green_button.clicked.connect(self.green_func)
        self.blue_button.clicked.connect(self.blue_func)
        self.stereopara_button.clicked.connect(self.stereopara_func)
        self.white_button.clicked.connect(self.white_func)
        self.black_button.clicked.connect(self.black_func)

    def open(self):
        try:
            self.red_slider.setValue(0)
            self.green_slider.setValue(0)
            self.blue_slider.setValue(0)
            self.rotation_slider.setValue(0)
            self.pixmap = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                                      'Картинка (*.jpg);;Картинка (*.png')[0]
            self.orig = Image.open(self.pixmap)
            self.curr = Image.open(self.pixmap)
            self.filtre_curr = Image.open(self.pixmap)
            self.pic = ImageQt(self.curr)
            self.pic_label.setPixmap(QPixmap(self.pixmap))
            self.pic_tr = True
            self.red_slider.setValue(0)
            self.green_slider.setValue(0)
            self.blue_slider.setValue(0)
        except Exception:
            pass

    def save_as(self):
        if self.pic_tr:
            try:
                save_name = \
                    QFileDialog.getSaveFileName(self, 'Сохранение фото', '', 'Картинка (*.png);;Картинка (*.jpeg)')[
                        0]
                self.curr.save(save_name)
            except Exception:
                pass

    def rotation_left(self):
        if self.pic_tr:
            btn = self.sender()
            self.degree += int(btn.text())
            degree = int(btn.text())
            self.degree %= 360
            self.curr = self.curr.rotate(degree, expand=True)
            self.filtre_curr = self.filtre_curr.rotate(degree, expand=True)
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
        else:
            pass

    def rotation_right(self):
        if self.pic_tr:
            btn = self.sender()
            self.degree -= int(btn.text())
            degree = 0 - int(btn.text())
            self.degree %= 360
            self.curr = self.curr.rotate(degree, expand=True)
            self.filtre_curr = self.filtre_curr.rotate(degree, expand=True)
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
        else:
            pass

    def rotation_slide(self):
        if self.pic_tr:
            self.curr = self.filtre_curr.copy()
            self.degree += self.rotation_slider.value()
            degree = self.rotation_slider.value()
            self.degree %= 360
            self.curr = self.curr.rotate(degree, expand=True)
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
        else:
            pass

    def white_func(self):
        if not self.white_tr:
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    if (r + g + b) >= 700:
                        pixels[i, j] = 255, 255, 255
            self.white_tr = True
            self.filtre_curr = self.curr.copy()
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)

    def black_func(self):
        if not self.black_tr:
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    if (r + g + b) <= 50:
                        pixels[i, j] = 0, 0, 0
            self.black_tr = True
            self.filtre_curr = self.curr.copy()
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)

    def stereopara_func(self):
        if not self.stereopara_tr:
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x - 1, 20 - 1, -1):
                for j in range(y):
                    rr = pixels[i - 20, j][0]
                    r, g, b = pixels[i, j]
                    pixels[i, j] = rr, g, b
            for i in range(20):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = 0, g, b
            self.filtre_curr = self.curr.copy()
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.stereopara_tr = True

    def mirror_horizont(self):
        if self.pic_tr:
            self.curr = self.curr.transpose(Image.FLIP_LEFT_RIGHT)
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def mirror_vertical(self):
        if self.pic_tr:
            self.curr = self.curr.transpose(Image.FLIP_TOP_BOTTOM)
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def red_change(self):
        if self.pic_tr:
            self.pc_cp = self.filtre_curr.copy()
            self.curr = self.pc_cp.rotate(self.rotation_slider.value(), expand=True).copy()
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = self.red_slider.value(), g, b

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
        else:
            pass

    def green_change(self):
        if self.pic_tr:
            self.pc_cp = self.filtre_curr.copy()
            self.curr = self.pc_cp.rotate(self.rotation_slider.value(), expand=True).copy()
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = r, self.green_slider.value(), b

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
        else:
            pass

    def blue_change(self):
        if self.pic_tr:
            self.pc_cp = self.filtre_curr.copy()
            self.curr = self.pc_cp.rotate(self.rotation_slider.value(), expand=True).copy()
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = r, g, self.blue_slider.value()

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
        else:
            pass

    def red_func(self):
        if self.pic_tr and not self.red_tr:
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = r, b, b
            self.filtre_curr = self.curr.copy()
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.red_tr = True

    def green_func(self):
        if self.pic_tr and not self.green_tr:
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = b, g, b
            self.filtre_curr = self.curr.copy()
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.green_tr = True

    def blue_func(self):
        if self.pic_tr and not self.blue_tr:
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = g, g, b
            self.filtre_curr = self.curr.copy()
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.blue_tr = True

    def all(self):
        if self.pic_tr:
            self.red_slider.setValue(0)
            self.green_slider.setValue(0)
            self.blue_slider.setValue(0)
            self.rotation_slider.setValue(0)
            self.curr = self.orig.copy()
            self.filtre_curr = self.orig.copy()
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.chb_tr = False
            self.negative_tr = False
            self.light_tr = False
            self.blur_tr = False
            self.contour_tr = False
            self.detail_tr = False
            self.edge_enhance_tr = False
            self.eem_tr = False
            self.emboss_tr = False
            self.find_edges_tr = False
            self.smooth_tr = False
            self.sharpen_tr = False
            self.red_tr = False
            self.green_tr = False
            self.blue_tr = False
            self.stereopara_tr = False
            self.white_tr = False
            self.black_tr = False
        else:
            pass

    def delete(self):
        def func_yes():
            self.chb_tr = False
            self.negative_tr = False
            self.light_tr = False
            self.blur_tr = False
            self.contour_tr = False
            self.detail_tr = False
            self.edge_enhance_tr = False
            self.eem_tr = False
            self.emboss_tr = False
            self.find_edges_tr = False
            self.smooth_tr = False
            self.sharpen_tr = False
            self.red_tr = False
            self.green_tr = False
            self.blue_tr = False
            self.stereopara_tr = False
            self.white_tr = False
            self.black_tr = False
            self.red_slider.setValue(0)
            self.green_slider.setValue(0)
            self.blue_slider.setValue(0)
            self.rotation_slider.setValue(0)
            self.pic_tr = False
            self.orig = ''
            self.curr = ''
            self.pic = ''
            self.filtre_curr = ''
            self.pic_label.setPixmap(QPixmap())
            dialog.close()

        if self.pic_tr:
            dialog = QDialog()
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.setWindowTitle('Вы уверены, что хотите удалить фото?')
            btn_yes = QPushButton('Да', dialog)
            btn_no = QPushButton('Нет', dialog)
            btn_yes.move(75, 50)
            btn_no.move(200, 50)
            btn_yes.clicked.connect(func_yes)
            btn_no.clicked.connect(lambda: dialog.close())
            dialog.exec()
        else:
            pass

    def chb(self):
        if self.pic_tr and not self.chb_tr:
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    bw = (r + g + b) // 3
                    pixels[i, j] = bw, bw, bw

            self.filtre_curr = self.curr.copy()
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.chb_tr = True
        else:
            pass

    def negative(self):
        if self.pic_tr and not self.negative_tr:
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = 255 - r, 255 - g, 255 - b

            self.filtre_curr = self.curr.copy()
            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.negative_tr = True
        else:
            pass

    def light(self):
        def curve(pixel):
            r, g, b = pixel
            brightness = r + g + b if r + g + b > 0 else 1
            if brightness < 60:
                k = 60 / brightness
                return min(255, int(r * k ** 2)), \
                       min(255, int(g * k ** 2)), \
                       min(255, int(b * k ** 2))
            else:
                return r, g, b

        if self.pic_tr and not self.light_tr:
            pixels = self.curr.load()
            x, y = self.curr.size
            for i in range(x):
                for j in range(y):
                    pixels[i, j] = curve(pixels[i, j])

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.light_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def blur(self):
        if self.pic_tr and not self.blur_tr:
            self.curr = self.curr.filter(ImageFilter.BLUR)

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.blur_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def contour(self):
        if self.pic_tr and not self.contour_tr:
            self.curr = self.curr.filter(ImageFilter.CONTOUR)

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.contour_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def detail(self):
        if self.pic_tr and not self.detail_tr:
            self.curr = self.curr.filter(ImageFilter.DETAIL)

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.detail_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def edge_enhance(self):
        if self.pic_tr and not self.edge_enhance_tr:
            self.curr = self.curr.filter(ImageFilter.EDGE_ENHANCE)

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.edge_enhance_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def eem(self):
        if self.pic_tr and not self.eem_tr:
            self.curr = self.curr.filter(ImageFilter.EDGE_ENHANCE_MORE)

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.eem_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def emboss(self):
        if self.pic_tr and not self.emboss_tr:
            self.curr = self.curr.filter(ImageFilter.EMBOSS)

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.emboss_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def find_edges(self):
        if self.pic_tr and not self.find_edges_tr:
            self.curr = self.curr.filter(ImageFilter.FIND_EDGES)

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.find_edges_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def smooth(self):
        if self.pic_tr and not self.smooth_tr:
            self.curr = self.curr.filter(ImageFilter.SMOOTH_MORE)

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.smooth_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass

    def sharpen(self):
        if self.pic_tr and not self.sharpen_tr:
            self.curr = self.curr.filter(ImageFilter.SHARPEN)

            self.pic = ImageQt(self.curr)
            self.pixmap = QPixmap.fromImage(self.pic)
            self.pic_label.setPixmap(self.pixmap)
            self.sharpen_tr = True
            self.filtre_curr = self.curr.copy()
        else:
            pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
