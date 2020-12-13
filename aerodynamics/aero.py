import numpy as np 
from numpy import cos, sin, arccos, pi,tan
import scipy.integrate as integrate
import pandas as pd
import os
import matplotlib.pyplot as plt 

class airfoil:
    def __init__(self,DNI,number_coefs,rudder= None):
        self.theta = np.linspace(0,pi,100) 
        self.dni = DNI
        self.n = number_coefs
        self.timon = rudder
        if self.rudder == None:
            self.T = 0
        elif self.rudder == 0:
            self.T = 1
        else:
            self.T = 2
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
        Coeficiente A0 para el perfil 
        """
        # Sin timon
        lim_inf = 0
        lim_sup = pi
        lim_medio = medio = arccos([(self.xf-0.5)*2])[0]
        tramo1 = integrate.quad(lambda x: self.f/(1-self.xf)**2*(2*self.xf-1-cos(x)),lim_inf,lim_medio)
        tramo2 = integrate.quad(lambda x: self.f/self.xf**2 *(2*self.xf-1-cos(x)),lim_medio,lim_sup)
        a0= -1/pi * (tramo1[0] + tramo2[0])
        # Solo timon
        lim_medio2 = arccos([((1-self.ca)-0.5)*2])[0]
        tramo1 = integrate.quad(lambda x: tan(self.delta_a),lim_inf,lim_medio2)
        a0_t = -1/pi * tramo1[0]
        self.a0 = np.array([a0,a0_t,a0+a0_t])
        return a0,a0_t,a0+a0_t
   
    def coefAN(self,n):
        """
        Coeficientes AN para el perfil sin timon
        """
        # Sin timon
        lim_inf = 0
        lim_sup = pi
        lim_medio = medio = arccos([(self.xf-0.5)*2])[0]
        tramo1 = integrate.quad(lambda x: (self.f/(1-self.xf)**2 * (2*self.xf-1-cos(x)))*cos(n*x),lim_inf,lim_medio)
        tramo2 = integrate.quad(lambda x: (self.f/self.xf**2 *(2*self.xf-1-cos(x)))*cos(n*x),lim_medio,lim_sup)
        an = -2/pi * (tramo1[0] + tramo2[0])
        # Solo timon
        lim_medio2 = arccos([((1-self.ca)-0.5)*2])[0]
        tramo1 = integrate.quad(lambda x: tan(self.delta_a)*cos(n*x),lim_inf,lim_medio2)
        an_t = -2/pi * tramo1[0]
    
        return an,an_t,an+an_t

    def coeficientes(self):
        """
        Returns all coeficientes from 0 to n
        """
        
        coefs = np.array([])
        a0 = self.coefAO()[self.T]
        coefs = np.append(coefs,a0)
        for index,coef in enumerate(self.n):
            an = self.coefAN(n = coef)[self.T]
            coefs = np.append(coefs,an)
        self.coefs = coefs
        np.savetxt("coefs.csv", coefs, delimiter=",")
        return coefs
    @coeficientes
    def lift_coef(self):
        """
        Returns the cl and cp of the airfoil
        """
        alpha_ST = - self.a0[self.T]
        x = 0.5+0.5*cos(self.theta)
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

        cl = 4*((alpha_ST+coefA0())*tan(self.theta/2)+sumAN(self.theta,self.coefs,self.n))
        cp = -cl/2
        self.cp,self.cl = cp,cl
        return cl, cp
    
    @coeficientes
    @lift_coef
    def plot_cp_cl(self):
        """
        Plots de cp and cl over the profile
        """
        fig , ax = plt.subplots()
        ax.plot(self.x,self.cp)
        ax.set_ylabel("Chord")
        ax.set_xlabel("Cp/cl")




        
    


