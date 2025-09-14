import pylab as pl
import numpy as np
x = np.array([50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240])
primerMetodoClasico = np.array([0.033518,0.050942,0.081182,0.120957,0.17208,0.235154,0.326483,0.407847,0.507917,0.649175,0.803968,1.00313,1.14931,1.38047,1.58018,1.87537,2.17496,2.56115,2.84365,3.32936])
segundoMetodoBloques = np.array([0.047534,0.079578,0.124794,0.191067,0.26349,0.374653,0.486543,0.640919,0.807765,1.0003,1.22917,1.51414,1.78535,2.1297,2.57103,2.94186,3.39424,3.95461,4.44629,5.11374])
pl.plot(x,primerMetodoClasico, linewidth=1.0, linestyle="-",label="primerMetodoClasico")
pl.plot(x,segundoMetodoBloques, linewidth=1.0, linestyle="-",label="segundoMetodoBloques")
pl.legend(loc='upper left')
pl.title('repeticiones=20 incremento=10')

pl.show()