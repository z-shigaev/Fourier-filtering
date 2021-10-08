import sys
import main_win
import plot_canvas as pc
import numpy as np
import math
import random as rnd
# import matplotlib.pyplot as plt
from numba import jit
from scipy.fft import rfft, rfftfreq
from PyQt5 import QtWidgets, QtGui
# from PyQt5.QtGui import QDoubleValidator as QDV
# from PyQt5.QtGui import QIntValidator as QIV

POINTS = 10000
FD = 25000
TIME = 10


class MainWindow(QtWidgets.QMainWindow, main_win.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.flag_filter = -1
        self.filter_signal = Plot()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QtGui.QIcon('main_icon.jpg'))
        self.list_func = ''
        self.x = [0, 1, 2, 4, 5, 6, 7]
        self.y = [0, 0, 0, 0, 0, 0, 0]
        self.base_array = Plot()
        self.frame1_layout = pc.Layout(self.frame_1, self.base_array.get_arrays()[0], self.base_array.get_arrays()[1])
        self.frame_1.setLayout(self.frame1_layout)
        self.frame2_layout = pc.Layout(self.frame_2, self.x, self.y)
        self.frame_2.setLayout(self.frame2_layout)
        self.frame3_layout = pc.Layout(self.frame_3, self.x, self.y)
        self.frame_3.setLayout(self.frame3_layout)
        # Сигналы кнопок
        self.btn_Add_func.clicked.connect(self.add_Function)
        self.btn_Reset_signal.clicked.connect(self.reset_signal)
        self.btn_Add_noise.clicked.connect(self.add_noise)
        self.btn_Filter.clicked.connect(self.filter)
        self.btn_OK_1.clicked.connect(self.image_1)
        self.btn_OK_2.clicked.connect(self.image_2)
        self.btn_OK_3.clicked.connect(self.image_3)
        # Сигналы виджетов
        self.lineEdit_FD.textEdited.connect(self.update_plot)
        self.lineEdit_points.textEdited.connect(self.update_plot)
        self.verticalSlider_1.sliderReleased.connect(self.slider1)
        self.verticalSlider_2.sliderReleased.connect(self.slider2)
        self.verticalSlider_3.sliderReleased.connect(self.slider3)
        # Настройки виджетов
        # self.lineEdit_min.setValidator(QIV(0, 9))
        # self.lineEdit_min.setValidator(QDV(1, 9999, 4, self))

    def add_Function(self):
        func = self.comboBox_func.currentText()
        A = self.lineEdit_coeff_A.text().replace(',', '.')
        B = self.lineEdit_coeff_B.text().replace(',', '.')
        str_func = func.replace("A", A)
        str_func = str_func.replace("B", B)
        self.list_func = self.list_func + str_func + "   "
        self.pTE_list_func.setPlainText('')
        self.pTE_list_func.setPlainText(self.list_func)
        self.base_array.add_function(func, A, B)
        self.frame1_layout.draw(self.base_array)
        self.frame_1.setLayout(self.frame1_layout)
        # Обновляем спектр частот
        self.signal_spectrum()
        # print(self.base_array.get_arrays())
        # print(func)
        # print("Успех")

    def add_noise(self):
        min = self.lineEdit_min.text()
        min_degree = self.comboBox_min.currentText()
        min = float(min) * 10 ** float(min_degree)
        # print(min)
        max = self.lineEdit_max.text()
        max_degree = self.comboBox_max.currentText()
        max = float(max) * 10 ** float(max_degree)
        # print(max)
        self.base_array.add_noise(min, max)
        if self.lineEdit_graph_1.text() != '':
            self.image_1()
        else:
            self.frame1_layout.draw(self.base_array)
            self.frame_1.setLayout(self.frame1_layout)
            self.signal_spectrum()

    def reset_signal(self):
        self.base_array.reset_arrays()
        self.frame1_layout.draw(self.base_array)
        self.frame_1.setLayout(self.frame1_layout)
        self.signal_spectrum()
        self.list_func = ''
        self.pTE_list_func.setPlainText('')

    def update_plot(self):
        if self.lineEdit_FD.text() == '':
            pass
        elif self.lineEdit_points.text() == '':
            pass
        else:
            global FD, POINTS
            FD = float(self.lineEdit_FD.text())
            POINTS = float(self.lineEdit_points.text())
            self.base_array.rewrite_arrays(fd=FD, points=POINTS)
            self.frame1_layout.draw(self.base_array)
            self.frame_1.setLayout(self.frame1_layout)

    def signal_spectrum(self):
        self.spectrum_y = rfft(self.base_array.get_arrays()[1])
        self.spectrum_y = (np.absolute(self.spectrum_y))/POINTS
        self.spectrum_x = rfftfreq(int(POINTS), 1/FD) # длина массива и 1/частота дискретизации
        self.spectrum_array = Spectrum(self.spectrum_x, self.spectrum_y)
        if self.lineEdit_graph_2.text() == '':
            self.frame2_layout.draw_spectrum(self.spectrum_array.get_arrays())
            self.frame_2.setLayout(self.frame2_layout)
        else:
            self.image_2()
        # print(TIME)

    def slider1(self):
        m = self.verticalSlider_1.value()
        self.lineEdit_per_1.setText(str(m))

    def slider2(self):
        m = self.verticalSlider_2.value()
        self.lineEdit_per_2.setText(str(m))

    def slider3(self):
        m = self.verticalSlider_3.value()
        self.lineEdit_per_3.setText(str(m))

    def image_1(self):
        x = float(self.lineEdit_graph_1.text())
        # print(x)
        percents = float(self.lineEdit_per_1.text())
        # print(percents)
        image_array = self.base_array.current_image(x, percents)
        if len(image_array[0]) == 0:
            pass
        else:
            self.frame1_layout.re_draw(image_array)
            self.frame_1.setLayout(self.frame1_layout)

    def image_2(self):
        x = float(self.lineEdit_graph_2.text())
        percents = float(self.lineEdit_per_2.text())
        self.spectrum_array.image(percents, x)
        image = self.spectrum_array.get_spectrum()
        if len(image[0]) == 0:
            pass
        else:
            self.frame2_layout.re_draw(image)
            self.frame_2.setLayout(self.frame2_layout)

    def image_3(self):
        x = float(self.lineEdit_graph_3.text())
        percents = float(self.lineEdit_per_3.text())
        image_array = self.filter_signal.current_image(x, percents)
        if len(image_array[0]) == 0:
            pass
        else:
            self.frame3_layout.re_draw(image_array)
            self.frame_3.setLayout(self.frame3_layout)

    def filter(self):
        trig_lvl = (float(self.lineEdit_trigger_level.text()))/2
        if self.flag_filter == -1:
            if trig_lvl == '':
                pass
            else:
                self.create_filter_signal(trig_lvl)
                self.frame3_layout.draw(self.filter_signal)
                self.frame_2.setLayout(self.frame3_layout)
                self.flag_filter = 1
        else:
            self.filter_signal.to_default()
            self.create_filter_signal(trig_lvl)
            self.frame3_layout.draw(self.filter_signal)
            self.frame_2.setLayout(self.frame3_layout)

    def create_filter_signal(self, trig_lvl):
        i = 0
        for m in self.spectrum_y:
            if m >= trig_lvl:
                ampl = 2*m
                print(ampl)
                freq = self.spectrum_x[i]
                print(freq)
                self.filter_signal.add_function('Asin(2*pi*Bx)', ampl, freq)
            else:
                pass
            i += 1



class Spectrum():
    def __init__(self, spectrum_x, spectrum_y):
        self.x = spectrum_x
        self.y = spectrum_y
        self.image_x = []
        self.image_y = []
        pass

    def get_arrays(self):
        return self.x, self.y

    def get_spectrum(self):
        return self.image_x, self.image_y

    def image(self, percents, val_x):
        half = percents/2
        length = len(self.x)
        if length == 0:
            pass
        else:
            index = -1
            left = self.x[0]
            i = 0
            if self.x[-1] < val_x:
                pass
            elif self.x[0] > val_x:
                pass
            else:
                for m in self.x:
                    if m == val_x:
                        index = i
                    else:
                        if m < val_x:
                            if self.x[i+1] > val_x:
                                index = i
                                break
                            else:
                                pass
                        else:
                            pass
                    i += 1
            if index == -1:
                pass
            else:
                bord_left = int(index - (half/100)*length)
                bord_right = int(index + (half/100)*length)
                if bord_left < 0:
                    bord_left = 0
                if bord_right > length:
                    bord_right = length
                self.image_x = self.x[bord_left:bord_right]
                self.image_y = self.y[bord_left:bord_right]


class Plot():
    def __init__(self):
        global POINTS
        global FD
        self.x_array = np.arange(float(POINTS))/float(FD)
        self.y_array = np.zeros(int(POINTS))
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.array_functions = []
        self.old_FD = 25000
        self.old_POINTS = 100000

    def to_default(self):
        global POINTS
        global FD
        self.x_array = np.arange(float(POINTS))/float(FD)
        self.y_array = np.zeros(int(POINTS))
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.array_functions = []
        self.old_FD = 25000
        self.old_POINTS = 100000


    def add_function(self, func, A, B):
        self.array_functions.append([func, A, B])
        self.add_one_function(func, A, B)

    def rewrite_arrays(self, fd=None, points=None):
        if fd != None:
            if points != None:
                self.old_FD = fd
                self.old_POINTS = points
        self.x_array = np.arange(float(POINTS))/float(FD)
        self.y_array = np.zeros(int(POINTS))
        for m in self.array_functions:
            self.add_one_function(m[0], m[1], m[2])

    @jit
    def add_one_function(self, func, A, B):
        # self.x_array = np.linspace(min, max, num=POINTS)
        i = 0
        if func == 'Asin(2*pi*Bx)':
            for m in self.x_array:
                a = self.y_array[i] + float(A) * math.sin(2*math.pi*float(B) * m)
                self.y_array[i] = a
                if m > self.x_max:
                    self.x_max = m
                if m < self.x_min:
                    self.x_min = m
                if a > self.y_max:
                    self.y_max = a
                if a < self.y_min:
                    self.y_min = a
                i += 1
            pass
        elif func == 'Acos(2*pi*Bx)':
            for m in self.x_array:
                a = self.y_array[i] + float(A) * math.cos(2*math.pi*float(B) * m)
                self.y_array[i] = a
                if m > self.x_max:
                    self.x_max = m
                if m < self.x_min:
                    self.x_min = m
                if a > self.y_max:
                    self.y_max = a
                if a < self.y_min:
                    self.y_min = a
                i += 1
            pass
        else:
            pass

    @jit
    def add_noise(self, min, max):
        i = 0
        for m in self.y_array:
            noise = rnd.uniform(float(min), float(max))
            self.y_array[i] = m + noise
            i += 1
            # print(noise)

    def reset_arrays(self):
        self.x_array = np.arange(float(POINTS))/float(FD)
        self.y_array = np.zeros(int(POINTS))
        self.array_functions = []

    def get_arrays(self):
        return self.x_array, self.y_array

    @jit
    def current_image(self, x, percents):
        if x == '':
            return [], []
        else:
            if x > self.x_array[-1]:
                return [], []
            elif x < self.x_array[0]:
                return [], []
            else:
                half_percents = percents / 2
                i = 0
                index = -1
                left = 0
                for m in self.x_array:
                    if m == x:
                        index = i
                        break
                    elif m < x:
                        left = m
                        if self.x_array[i+1] > x:
                            index = i
                            break
                    i += 1
                length = len(self.x_array)
                step = (half_percents/100)*length
                bord_left = index - step
                print(bord_left)
                bord_right = index + step
                print(bord_right)
                if int(bord_right) > length:
                    bord_right = length
                if int(bord_left) < 0:
                    bord_left = 0
                self.image_x = self.x_array[int(bord_left):int(bord_right)]
                self.image_y = self.y_array[int(bord_left):int(bord_right)]
                print(self.image_x)
                return self.image_x, self.image_y


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()