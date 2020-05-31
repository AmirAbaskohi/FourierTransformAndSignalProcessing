import matplotlib.pyplot as plt
import scipy.fftpack
import numpy as np
import csv
x = list()
y = list()
firstLine = True
with open('data.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		if firstLine:
			firstLine = False
			continue
		x.append(float(row[0]))
		y.append(float(row[1]))
plt.plot(x,y)
plt.title("RXJ0806.3+1527")
plt.xlabel("ΔTime(s)")
plt.ylabel("Count Rate(counts/s)")
yf = np.fft.fft(y)
freq = np.fft.fftfreq(len(y),x[1]-x[0])
plt.figure()
plt.plot(freq,np.abs(yf))
plt.xlabel("Frequency (HZ)")
plt.ylabel("Magnitude")
plt.show()