import sys
import main_win
import plot_canvas as pc
import numpy as np
import math
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtGui


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
        self.frame1_layout.draw(self.base_array.get_arrays()[0], self.base_array.get_arrays()[1])
        self.frame_1.setLayout(self.frame1_layout)
        # print(self.base_array.get_arrays())
        # print(func)
        # print("Успех")


class Plot():
    def __init__(self):
        self.x_array = np.linspace(0, 10, num=100)
        self.y_array = np.zeros(100)

    def add_function(self, func, A, B):
        i = 0
        if func == 'Asin(Bx)':
            for m in self.x_array:
                a = self.y_array[i] + float(A)*math.sin(float(B)*m)
                self.y_array[i] = a
                i += 1
            pass
        else:
            pass
        print(self.y_array)
    # for m in self.x_array:
    #     a = math.sin(m)
    #     self.y_array.append(a)
    # pass

    def get_arrays(self):
        return self.x_array, self.y_array






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()