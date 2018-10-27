import matplotlib.pyplot as plt
import numpy as np

print "La implementacion no me da igual que la fft. Solo hago un FOR para los tiempos"
def expo(t, puntos, w):
	#parte exponencial
	e = np.exp((-np.pi)*t*2j*w/(1.0*puntos))
	cs = np.cos((-2.0*t*np.pi*w)/(puntos*1.0)) + (1j*np.sin((-2.0*t*np.pi*w)/(puntos*1.0)) )
	return e


def fourier (funcion , puntos, w):
	lista = []
	suma = 0.0
	for i in range(0,puntos-1):
		#suma += funcion[i] * expo(i, puntos, w)
		lista.append( funcion * expo(i, puntos, w) )
		suma += funcion[i] * expo(i, puntos, w)
	return suma
	#return lista
