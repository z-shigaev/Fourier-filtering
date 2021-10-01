import random
from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QTableWidgetItem

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

class Layout(QVBoxLayout):
    def __init__(self,root, x, y):
        super().__init__()
        plt.style.use("seaborn-dark")
        self.x = x
        self.y = y
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(x, y)
        self.canvas = FigureCanvas(self.figure)
        self.addWidget(self.canvas)

    def draw(self, new_x, new_y):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.x = new_x
        self.y = new_y
        self.ax.plot(self.x, self.y)
        self.canvas.draw()