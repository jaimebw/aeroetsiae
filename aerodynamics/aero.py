import numpy as np 
from numpy import cos, sin, arccos, pi,tan
import scipy.integrate as integrate
import pandas as pd


class airfoil:
    def __init__(self,DNI,number_coefs):
        self.dni = DNI
        self.n = number_coefs
        try:
            self.f = 1 + int(int(self.dni[3])*5/8)/100
            self.xf = 20 + 10*int(int(self.dni[4])/8*2)/100
            self.t = 8 +int(int(self.dni[5])*10/9)/100
            self.ca = 20 +5*int(int(self.dni[6])*3/8)/100
            self.delta_a = np.radians(-(5 + 5*int(int(self.dni[7])*2/8)))
            #self.parametros = np.array([self.f,self.xf,self.t,self.ca,self.delta_a])/100
        except ValueError:
            print("DNI no valido, revisa que las cifras son correctas, no pongas la letra del final")
        


    def __repr__(self):
        return  "NACA Airfoil {}{}{}".format(str(self.f*100),str(self.xf*100)[0],str(self.t*100))
        #print("Tu perfil NACA es el",str(f),str(xf)[0],str(t))

    def coefAO(self):
        # Coeficiente A0 para el perfil sin timon
        lim_inf = 0
        lim_sup = pi
        lim_medio = medio = arccos([(self.xf-0.5)*2])[0]
        tramo1 = integrate.quad(lambda x: self.f/(1-self.xf)**2*(2*self.xf-1-cos(self.x)),lim_inf,lim_medio)
        tramo2 = integrate.quad(lambda x: self.f/self.xf**2 *(2*self.xf-1-cos(self.x)),lim_medio,lim_sup)
        self.a0 = -1/pi * (tramo1[0] + tramo2[0])
        return self.a0
    


