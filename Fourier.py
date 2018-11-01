import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
from scipy.fftpack import fft, ifft, fftfreq


def expo(t, puntos, w):
	#parte exponencial
	e = np.exp((-np.pi)*t*2j*w/(1.0*puntos))
	cs = np.cos((-2.0*t*np.pi*w)/(puntos*1.0)) + (1j*np.sin((-2.0*t*np.pi*w)/(puntos*1.0)) )
	return e


def fourier (funcion , puntos, w):
	lista = []
	suma = 0.0
	for j in range (0,len(funcion)):
		for w in range(0,puntos-1):
			suma += funcion[j] * expo(j, puntos, w)
		lista.append(suma)
		suma= 0.0
	return lista
	#return lista


#prueba con array
lista = np.linspace(1.0 ,10.0 ,30)
Flista = fourier(lista, 30 , 1.0)
#print lista
#print "  "
#print Flista


#------- intento con Pandas
#df = pd.read_csv('datos.txt', names=['x','y']) 
#print df.head() 
#x = df.loc[:, ['x']].values 
#y = df.loc[:,['y']].values


#-------- intento solo con readlines
#archivo = open("signal.dat",'rw')
#nuevo = open("signall.dat",'w')
#for mensaje in archivo:
 	#mensaje = archivo.readline()#
 	#mensaje.replace(',', ' ')
	#nuevo.write(mensaje)

#------- intento con openfile
#mensaje = archivo.readline()
#mensaje.replace(",", "")
#nuevo.write(mensaje)
#archivo.close()
#nuevo.close()


  
datos = np.genfromtxt("signal.dat", dtype=None,names = ['x','y'], delimiter=",")
x = np.genfromtxt("signal.dat", usecols=0)
y = np.genfromtxt("signal.dat", usecols=2) #la columna uno son las comas

#print "longit. datos: ", len(x)
#print y
#print datos
#---------------------------------------------------------------------------------
plt.figure()
plt.plot(x,y)
plt.savefig("ArguelloDiego_signal.pdf")
plt.close()


#print fourier(y , 10 , 1)[0:3]

Flista = fourier(y, 10, 1)
real = fft(y)
frecu = fftfreq(512,1)
#print real[0:3]
#print Flista[0:3]

plt.plot(frecu,real)
plt.xlim(-0.1, 0.1)
#plt.show()
#plt.plot(frecu,Flista)
plt.show()


plt.xlim(-5, 5)
plt.savefig("ArguelloDiego_TF.pdf")

real[frecu > 0.03] = 0
real[frecu < -0.03] = 0
#--------- solo para probar
#plt.plot(frecu , real)
#plt.xlim(-0.1,0.1)
#plt.show()

filtrada = np.fft.ifft(real)
plt.plot(x , filtrada)
plt.xlim(0.0,0.04)
plt.savefig("ArguelloDiego_filtrada.pdf")


