import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft, fftfreq, fft2

#---------------intentos con distintas herramientas
#from skiimage import io
#arbol = io.imread("Arboles.png")
#print("forma: ")
#print(image.shape)
#plt.figure()
#plt.imshow(arbol,vmin=0,vmax=1)

#I = np.asarray(PIL.Image.open('Arboles.npg'))
#print I

import PIL
arbol = PIL.Image.open('Arboles.png').convert("L")

Larbol = np.array(arbol)
print Larbol
fourier = fft2(Larbol)
freq = fftfreq(10, 1)

x = np.arange(-256, 256, 1)
y = np.arange(-256, 256, 1)
X, Y = np.meshgrid(x, y)
#plt.imshow(fourier.real)
plt.imshow(np.log10(abs(fourier) ))
plt.colorbar();
#----------------------------------------------------------
#plt.savefig("ArguelloDiego_FT2D.pdf")
