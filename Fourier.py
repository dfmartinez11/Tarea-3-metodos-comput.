import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd

def expo(t, puntos, frec):
	#parte exponencial
	e = np.exp((-2.0j*t*np.pi*frec)/(puntos*1.0))
	cs = np.cos((-2.0*t*np.pi*frec)/(puntos*1.0)) + (1j*np.sin((-2.0*t*np.pi*frec)/(puntos*1.0)) )
	return cs

def fourier (funcion , puntos, frec):
	suma = 0.0
	for i in range(0,puntos-1):
	#	suma += funcion[i] * expo(i, puntos, frec)
		suma += funcion * expo(i, puntos, frec)
	return suma

#prueba con array
lista = np.linspace(1.0 ,10.0 ,30)
Flista = fourier(lista, 30 , 1.0)
#print lista
#print "  "
#print Flista

#archivo = np.loadtxt("signal.dat")
#print archivo
#df = pd.read_csv('datos.txt', names=['x','y']) 
#print df.head() 
#x = df.loc[:, ['x']].values 
#y = df.loc[:,['y']].values

#archivo = open("signal.dat",'rw')
#nuevo = open("signall.dat",'w')
#for mensaje in archivo:
 	#mensaje = archivo.readline()#
 	#mensaje.replace(',', ' ')
	#nuevo.write(mensaje)

#mensaje = archivo.readline()
#mensaje.replace(",", "")
#nuevo.write(mensaje)


#archivo.close()
#nuevo.close()

#f=np.opentxt("signal.dat") 
#print f
  
datos = np.genfromtxt("signal.dat", dtype=None,names = ['x','y'], delimiter=",")
print datos




