from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Comic Sans MS, Arial'
FD = 250000#частота дискретизации, отсчётов в секунду
N = 2500#длина входного массива, N/FD секунд 
F=100000.0#циклическая частота входного сигнала
w=(2.*pi*F/FD)#отсчёт круговой частоты 
A=3.0#амплитуда сигнала
B=0.5#порог ограничения
#сгенерируем чистый синусоидальный сигнал с частотой F длиной N
sin_sig = array([A*sin(w*t) for t in range(N)])#график сигнала
plt.plot(arange(N)/float(FD), sin_sig, 'r')
plt.xlabel('Время, сек.')
plt.ylabel('Амплитуда  сигнала')
plt.title('Входной синусоидальный сигнала')
plt.grid(True)
plt.show()
spectr_sin = rfft(sin_sig )#вычисляем дискретное действительное rfft  преобразование Фурье
plt.plot(rfftfreq(N, 1./FD), np_abs(spectr_sin)/N) #график спектра
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда  сигнала')
plt.title('Спектр синусоидального сигнала')
plt.grid(True)
plt.show()