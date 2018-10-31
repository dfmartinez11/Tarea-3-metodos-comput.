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
