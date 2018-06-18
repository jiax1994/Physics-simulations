''' ceci est un programme qui affiche le figure 2.1'''

#importation du module numpy
import numpy as np

#importation de la librairie matplotlib
import matplotlib.pyplot as plt

#la valeur de x est définie entre 0.0 et 5.0 avec un pas de 0.1
x=np.arange(0.0,5.0,0.1)

#dfinir y1 y2 y3 et y4
y1=1.5*(1-np.exp(-x))
y2=2*(1-np.exp(-x))
y3=3*(1-np.exp(-x))
y4=x

#créer des courbes de x avec y1 y2 y3 et y4
plt.plot(x,y1,'b', label='f(x)=1.5*(1-np.exp(-x))')
plt.plot(x,y2,'g', label='f(x)=2*(1-np.exp(-x))')
plt.plot(x,y3,'r', label='f(x)=3*(1-np.exp(-x))')
plt.plot(x,y4,'k--', label='f(x)=x')

#les axes sont entre 0.0 et 4.0
plt.axis([0.0,4.0,0.0,4.0])

#donner les noms des axes
plt.xlabel('x')
plt.ylabel('f(x)')

#créer une légende 
plt.legend(loc='upper left')
plt.grid()

#montrer la courbe
plt.show()
