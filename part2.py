import matplotlib.pyplot as plt
import numpy as np
import math
import csv
EWx = list()
EWy = list()
NSx = list()
NSy = list()
UDx = list()
UDy = list()
with open('elcentro_EW.dat', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=" ")
	for row in plots:
		EWx.append(float(row[0]))
		EWy.append(float(row[1]))
with open('elcentro_NS.dat', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=" ")
	for row in plots:
		NSx.append(float(row[0]))
		NSy.append(float(row[1]))
with open('elcentro_UP.dat', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=" ")
	for row in plots:
		UDx.append(float(row[0]))
		UDy.append(float(row[1]))
plt.subplot(3,1,1)
plt.plot(EWx, EWy)
plt.title("EW")
plt.ylabel("Acceleration[g]")
plt.subplot(3,1,2)
plt.plot(NSx, NSy)
plt.title("NS")
plt.ylabel("Acceleration[g]")
plt.subplot(3,1,3)
plt.plot(UDx, UDy)
plt.ylabel("Acceleration[g]")
plt.title("UD")
plt.xlabel("Time[sec]")
plt.show()
PGA = max(NSy)
intesity = 3*(math.log10(PGA)+0.5)
print(PGA)
print(intesity)
FNSy = np.fft.fft(NSy)
freq = np.linspace(0.0,1.0/(2.0*(NSx[1]-NSx[0])),len(FNSy)/2)
plt.figure()
plt.plot(freq, 2.0/len(FNSy)*np.abs(FNSy[:len(FNSy)//2]))
plt.ylabel("Magnitude")
plt.xlabel("Frequency[Hz]")
plt.show()
PerdominantFrequency = max(FNSy)
print(np.abs(PerdominantFrequency))
plt.specgram(NSy,Fs=int(1.0/(NSx[1]-NSx[0])),NFFT=1024,noverlap=900)
plt.show()