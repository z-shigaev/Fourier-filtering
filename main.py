import sys
import main_win
import plot_canvas as pc
import numpy as np
import math
import random as rnd
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QDoubleValidator as QDV
from PyQt5.QtGui import QIntValidator as QIV

POINTS = 100000
TIME = 10


class MainWindow(QtWidgets.QMainWindow, main_win.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QtGui.QIcon('main_icon.jpg'))
        self.list_func = ''
        self.x = [0, 1, 2, 4, 5, 6, 7]
        self.y = [1, 2, 3, 4, 3, 2, 1]
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
        self.btn_Filter.clicked.connect(self.signal_spectrum)
        # Сигналы виджетов
        self.lineEdit_min_time.textEdited.connect(self.update_plot)
        self.lineEdit_max_time.textEdited.connect(self.update_plot)
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
        min = float(self.lineEdit_min_time.text())
        max = float(self.lineEdit_max_time.text())
        self.base_array.add_function(func, A, B, min, max)
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
        self.frame1_layout.draw(self.base_array)
        self.frame_1.setLayout(self.frame1_layout)

    def reset_signal(self):
        self.base_array.reset_arrays()
        self.frame1_layout.draw(self.base_array)
        self.frame_1.setLayout(self.frame1_layout)
        self.list_func = ''
        self.pTE_list_func.setPlainText('')

    def update_plot(self):
        if self.lineEdit_min_time.text() == '':
            pass
        elif self.lineEdit_min_time.text() == '-':
            pass
        elif self.lineEdit_max_time.text() == '':
            pass
        elif self.lineEdit_max_time.text() == '-':
            pass
        else:
            min = float(self.lineEdit_min_time.text())
            max = float(self.lineEdit_max_time.text())
            global TIME
            TIME = max - min
            self.base_array.rewrite_arrays(min=min, max=max)
            self.frame1_layout.draw(self.base_array)
            self.frame_1.setLayout(self.frame1_layout)

    def signal_spectrum(self):
        self.spectrum_y = rfft(self.base_array.get_arrays()[1])
        self.spectrum_y = (np.absolute(self.spectrum_y))/POINTS
        self.spectrum_x = rfftfreq(POINTS, TIME/POINTS) # длина массива и 1/частота дискретизации
        spectrum_array = self.spectrum_x, self.spectrum_y
        self.frame2_layout.draw_spectrum(spectrum_array)
        self.frame_2.setLayout(self.frame2_layout)
        # print(TIME)


class Plot():
    def __init__(self):
        global POINTS
        self.x_array = np.linspace(0, 10, num=POINTS)
        self.y_array = np.zeros(POINTS)
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.array_functions = []
        self.old_min_time = 0
        self.old_max_time = 10

    def add_function(self, func, A, B, min, max):
        self.array_functions.append([func, A, B])
        if self.old_min_time != min or self.old_max_time != max:
            self.old_min_time = min
            self.old_max_time = max
            self.rewrite_arrays()
        else:
            self.add_one_function(func, A, B)
        # self.array_functions.append([func, A, B])

        # print(self.y_array)
    # for m in self.x_array:
    #     a = math.sin(m)
    #     self.y_array.append(a)
    # pass

    def rewrite_arrays(self, min=None, max=None):
        if min != None:
            if max != None:
                self.old_min_time = min
                self.old_max_time = max
        self.x_array = np.linspace(self.old_min_time, self.old_max_time, num=POINTS)
        self.y_array = np.zeros(POINTS)
        for m in self.array_functions:
            self.add_one_function(m[0], m[1], m[2])

    def add_one_function(self, func, A, B):
        # self.x_array = np.linspace(min, max, num=POINTS)
        i = 0
        if func == 'Asin(Bx)':
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
        elif func == 'Acos(Bx)':
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

    def add_noise(self, min, max):
        i = 0
        for m in self.y_array:
            noise = rnd.uniform(float(min), float(max))
            self.y_array[i] = m + noise
            i += 1
            # print(noise)

    def reset_arrays(self):
        self.x_array = np.linspace(self.old_min_time, self.old_max_time, num=POINTS)
        self.y_array = np.zeros(POINTS)

    def get_arrays(self):
        return self.x_array, self.y_array


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()