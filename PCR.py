import matplotlib.pyplot as plt
import numpy as np
import urllib2

url = "http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat"
archivo = urllib2.urlopen(url)

#datos.split(",")
#print datos.split(",")
#print float(datos.split(",")[3])

lineas = archivo.readlines()
longitud=len(lineas)

#total = np.array([])
total = []

#print archivo.readline()
for i in  lineas:
	
	lista = i.split(",")
	if lista[1]=="B": lista[1]="1"
	if lista[1]=="M": lista[1]="2"
	for j in range(len(lista)) :
		lista[j] = float(lista[j])
	total.append(lista)

#print total[0]
matriz = np.array(total)
Matriz = matriz.transpose()

#print Matriz[1]
#print Matriz.shape[0]

var=[]
for i in range(Matriz.shape[0]):
	prom = np.mean(Matriz[i,:])
	varr = 0.0
	for j in range(Matriz.shape[1]):
		Matriz[i,j] = (Matriz[i,j]- prom)/(0.1*(Matriz.shape[1]-1) )
		varr += (Matriz[i,j]**2)
	var.append(varr**0.5)
	for j in range(Matriz.shape[1]):
		Matriz[i,j] = Matriz[i,j]/(varr**0.5)
		

covar = np.cov(Matriz)
print "---------fila 0 real"
print covar[0:2]

covar=np.ones((Matriz.shape[0] , Matriz.shape[0] ))
for i in range(Matriz.shape[0]):
	for j in range(Matriz.shape[0]):
		covar[i,j] = np.dot( Matriz[i,:],Matriz[j,:] )
		

print "---------fila 0 implementada"
print covar[0:2]

	

	
	
