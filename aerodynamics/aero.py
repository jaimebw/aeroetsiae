import numpy as np 
from numpy import cos, sin, arccos, pi,tan
import scipy.integrate as integrate
import pandas as pd
import os

class airfoil:
    def __init__(self,DNI,number_coefs):
        self.theta = np.linspace(0,pi,100) 
        self.dni = DNI
        self.n = number_coefs
        if not os.path.exists("airfoil_data"):
            os.mkdir("airfoil_data")
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
   


    def coefAO(self):
        """
        Coeficiente A0 para el perfil sin timón
        """
        lim_inf = 0
        lim_sup = pi
        lim_medio = medio = arccos([(self.xf-0.5)*2])[0]
        tramo1 = integrate.quad(lambda x: self.f/(1-self.xf)**2*(2*self.xf-1-cos(x)),lim_inf,lim_medio)
        tramo2 = integrate.quad(lambda x: self.f/self.xf**2 *(2*self.xf-1-cos(x)),lim_medio,lim_sup)
        a0= -1/pi * (tramo1[0] + tramo2[0])
        return a0
    def coefAN(self,n):
        # Coeficientes AN para el perfil sin timon
        lim_inf = 0
        lim_sup = pi
        lim_medio = medio = arccos([(self.xf-0.5)*2])[0]
        tramo1 = integrate.quad(lambda x: (self.f/(1-self.xf)**2 * (2*self.xf-1-cos(x)))*cos(n*x),lim_inf,lim_medio)
        tramo2 = integrate.quad(lambda x: (self.f/self.xf**2 *(2*self.xf-1-cos(x)))*cos(n*x),lim_medio,lim_sup)
        an = -2/pi * (tramo1[0] + tramo2[0])
        return an

    def coeficientes(self):
        """
        Returns all coeficientes from 0 to n
        """
        coefs = np.array([])
        a0 = self.coefAO()
        coefs = np.append(coefs,a0)
        for index,coef in enumerate(self.n):
            an = self.coefAN(n = coef)
            coefs = np.append(coefs,an)
        self.coefs = coefs
        np.savetxt("coefs.csv", coefs, delimiter=",")
        return coefs
    @coeficientes
    def lift_coef(self):
        def sumAN(theta,coefn,n):
            Sumatorio = np.array([])
            
            for count,i in enumerate(theta):
                
                sumatorio = 0
                
                for count2,j in enumerate(n):
                    if count2 == 0:
                        continue
                    else :
                        sumatorio += CoefAN[count2]*np.sin(int(count2)*i)
                Sumatorio = np.append(Sumatorio,sumatorio)
            return Sumatorio
        
    


