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
	if lista[1]=="B": lista[1]="1.0"
	if lista[1]=="M": lista[1]="2.0"
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
		

covar=np.ones((Matriz.shape[0] , Matriz.shape[0] ))
for i in range(Matriz.shape[0]):
	for j in range(Matriz.shape[0]):
		covar[i][j] = np.sum(np.dot( Matriz[i],Matriz[j] ))
		

print "---------fila 0 implementada mia"
print covar[0:2]

covar2 = np.cov(Matriz)
print "---------fila 0 real"
print covar2[0:2]


diagonaliz = np.linalg.eig(covar)
#vect = np.matmul(Matriz.transpose,diagonaliz[1][0])
#print vect

valores = diagonaliz[0]
vectores = diagonaliz[1]
for i in range(valores.shape[0]):
	print "_____________",i," :","\n","----valor= ", valores[i],"\n","----Vector [0:3]= ", vectores[i][0:3]

print " "
print "Los vectores mas importantes son aquellos que estan relacionados con los valores propios de mayor magnitud; puesto que significa que estos vectores son una base mas apropiada para escribir los datos"

# estos son los datos proyectados en los autovectores, solo se  multiplican las matrices

#nuevaM = np.matmul(vectores , Matriz)
PC1 = vectores[19]
PC2 = vectores[20]
print PC1.transpose().shape

proy1 = np.matmul(Matriz.transpose(),PC1)
proy2 = np.matmul(Matriz.transpose(),PC2)
#print proy1.transpose()[0:5]
#print proy2.transpose()[0:5]

plt.figure()
plt.scatter(proy1, proy2)
plt.savefig("ArguelloDiego_PCA.pdf")




