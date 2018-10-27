import matplotlib.pyplot as plt
import numpy as np
covar=np.ones((Matriz.shape[0] , Matriz.shape[0] ))
for i in range(Matriz.shape[0]):
	for j in range(Matriz.shape[0]):
		covar[i,j] = np.dot( Matriz[i,:],Matriz[j,:] )
		

print "---------fila 0 implementada NO es igual a la real"
print covar[0:2]

covar = np.cov(Matriz)
print "---------fila 0 real"
print covar[0:2]


diagonaliz = np.linalg.eig(covar)
#vect = np.matmul(Matriz.transpose,diagonaliz[1][0])
#print vect

valores = diagonaliz[0]
vectores = diagonaliz[1]
