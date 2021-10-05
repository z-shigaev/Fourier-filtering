import sys
import main_win
import plot_canvas as pc
import numpy as np
import math
import random as rnd
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtGui

POINTS = 1000


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
        self.btn_Add_func.clicked.connect(self.add_Function)
        self.btn_Reset_signal.clicked.connect(self.reset_signal)
        self.btn_Add_noise.clicked.connect(self.add_noise)

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
        # print(self.base_array.get_arrays())
        # print(func)
        # print("Успех")

    def add_noise(self):
        min = self.lineEdit_min.text()
        max = self.lineEdit_max.text()
        self.base_array.add_noise(min, max)
        self.frame1_layout.draw(self.base_array)
        self.frame_1.setLayout(self.frame1_layout)

    def reset_signal(self):
        self.base_array.reset_arrays()
        self.frame1_layout.draw(self.base_array)
        self.frame_1.setLayout(self.frame1_layout)
        self.list_func = ''
        self.pTE_list_func.setPlainText('')




class Plot():
    def __init__(self):
        global POINTS
        self.x_array = np.linspace(0, 10, num=POINTS)
        self.y_array = np.zeros(POINTS)
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0

    def add_function(self, func, A, B):
        i = 0
        if func == 'Asin(Bx)':
            for m in self.x_array:
                a = self.y_array[i] + float(A)*math.sin(float(B)*m)
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
                a = self.y_array[i] + float(A)*math.cos(float(B)*m)
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
        print(self.y_array)
    # for m in self.x_array:
    #     a = math.sin(m)
    #     self.y_array.append(a)
    # pass

    def add_noise(self, min, max):
        i = 0
        for m in self.y_array:
            noise = rnd.uniform(float(min), float(max))
            self.y_array[i] = m + noise
            i += 1
            print(noise)



    def reset_arrays(self):
        self.x_array = np.linspace(0, 10, num=POINTS)
        self.y_array = np.zeros(POINTS)

    def get_arrays(self):
        return self.x_array, self.y_array


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()