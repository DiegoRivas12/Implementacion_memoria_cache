import pylab as pl
import numpy as np
x = np.array([20,70,120,170,220,270,320,370,420,470,520,570,620,670,720,770,820,870,920,970])
primerMetodo = np.array([0.00053,0.000836,0.002993,0.005262,0.00823,0.012973,0.019478,0.025877,0.031654,0.040144,0.047124,0.055886,0.067008,0.078675,0.089201,0.102122,0.115528,0.131849,0.149948,0.166257])
segundoMetodo = np.array([0.000433,0.000821,0.002708,0.005361,0.008646,0.013061,0.019012,0.025583,0.034752,0.041992,0.052414,0.063013,0.076086,0.085709,0.097218,0.110069,0.128167,0.168204,0.185966,0.193366])
pl.plot(x,primerMetodo, linewidth=1.0, linestyle="-",label="primerMetodo")
pl.plot(x,segundoMetodo, linewidth=1.0, linestyle="-",label="segundoMetodo")
pl.legend(loc='upper left')
pl.title('repeticiones=20 incremento=50')

pl.show()