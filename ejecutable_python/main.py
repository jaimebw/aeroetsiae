__author__ = "Jaime Bowen"
__copyright__ = "Copyright 2020, jaimebw"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Jaime Bowen"
__email__ = "jaimebwv@gmail.com"
from modulo.funciones import *
import tkinter as tk
import numpy as np
import os
from numpy import cos, arccos, pi,tan
import scipy.integrate as integrate
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

ventana = tk.Tk()
ventana.title("Aerodinámica")
ventana.geometry("700x100")
lbl0 = tk.Label(ventana,text = "Programa para el cálculo de los coeficientes de la Teoría Potencial Linealizada")
lbl1 = tk.Label(ventana,text="Introduce tu DNI")
lbl2 = tk.Label(ventana)
lbl3 = tk.Label(ventana)
txt = tk.Entry(ventana,width=10)
lbl0.grid(column=0, row=0)
lbl1.grid(column=0, row=1)
lbl2.grid(column=1, row=2)
lbl3.grid(column = 3,row = 2)
txt.grid(column=0, row=2)
res = "h"
def pulsar():
    global res
    def perfilnacaboton(DNI):
        # genera los parámetros del perfil
        """
        123VWXYZ
        01234567
        """
        try:
            f = 1 + int(int(DNI[3]) * 5 / 8)
            xf = 20 + 10 * int(int(DNI[4]) / 8 * 2)
            t = 8 + int(int(DNI[5]) * 10 / 9)

            return print("Tu perfil NACA es el", str(f), str(xf)[0], str(t))
        except:
            print("Error ")
    res = txt.get()
    lbl0.destroy()
    lbl1.destroy()
    lbl2.configure(text = "DNI Obtenido")
    lbl3.configure(text= perfilnacaboton(res))
    txt.destroy()
    btn.destroy()
    #ventana.quit()


    print("DNI Obtenido")
btn = tk.Button(ventana, text="Enter",command = pulsar)
btn.grid(column=1, row=2)

ventana.mainloop()



dni = res



carpeta_datos_csv = r"datos_csv/"
if not os.path.exists(carpeta_datos_csv):
    os.mkdir(carpeta_datos_csv)




parametros_perfil = perfilnaca(dni)

f = parametros_perfil[0]
xf = parametros_perfil[1]
t = parametros_perfil[2]
ca = parametros_perfil[3]
delta_a = np.radians(-parametros_perfil[4]*100)

numero_coeficientes = 250 # número de coeficientes
xa = 1 -ca
n = np.linspace(0,numero_coeficientes,numero_coeficientes+1)
# coefcientes de glauert perfil sin timon
Coeficientes_n = pd.DataFrame()
CoefAN_ST = np.array([])
count = 0
coef = 0
for count,i in enumerate(n):
    if count == 0:
        coef = coefA0(xf,f)
        CoefAN_ST = np.append(CoefAN_ST,coef) # ojo, que casi la cagas por esto: no lo quites, porque sino A0 no se pone dentro del vector para el calculo del Cl
    else:
        coef = coefAN(int(count),xf,f)
        CoefAN_ST = np.append(CoefAN_ST,coef)
    coeficientes_n = pd.DataFrame({"Coeficientes Sin Timon":"A"+str(count),"A":coef},index = [count])
    Coeficientes_n= Coeficientes_n.append(coeficientes_n)
guardarcsv(Coeficientes_n,"coeficientes__glauert_sin_timon")

# coeficiente de glauert perfil con timon
CoeficientesT = pd.DataFrame()
CoefAN_CT = np.array([])
count = 0
for count,i in enumerate(n):
    if count == 0:
        coef = coefA0_T(xf,f)
        CoefAN_CT = np.append(CoefAN_CT,coef)
    else:
        coef = coefAN_T(ca,delta_a,int(count))
        CoefAN_CT = np.append(CoefAN_CT,coef)
    coeficientesT = pd.DataFrame({"Coeficientes Solo Timon":"A"+str(count),"A":coef},index = [count])
    CoeficientesT = CoeficientesT.append(coeficientesT)
guardarcsv(CoeficientesT,"coeficientes_glauert_solo_timon")

n1 = np.linspace(0,numero_coeficientes,numero_coeficientes)# ojito con este coeficiente, dado que las dimensiones se pueden ir a la mierda en caso de que se toque

theta = np.linspace(0,pi,100) # variable independiente
x = 0.5+0.5*cos(theta) # e
alpha_ST =np.array([-coefA0(xf,f)])  # alpha, angulo de ataque

for i in alpha_ST:
    cl_ST = 4*((i+coefA0(xf,f))*tan(theta/2)+sumAN(theta,CoefAN_ST,n1))
    cp_ST = -cl_ST/2
cL_ST = pd.DataFrame({"Eje X":x,"Eje Theta":theta,"Cl(alpha="+ str(round(np.degrees(alpha_ST[0]),2))+")":cl_ST,"Cp(alpha="+ str(round(np.degrees(alpha_ST[0]),2))+")":cp_ST})
guardarcsv(cL_ST,"datoscl_solo_perfil")

alpha_T = np.array([-coefA0(xf,f)])

CL_CP_T = pd.DataFrame()
for count,i in enumerate(alpha_T):
    cl_T = 4*((i+CoefAN_CT[0])*tan(theta/2)+sumAN(theta, CoefAN_CT ,n1))
    cp_T = -cl_T /2

cL_CT = pd.DataFrame({"Eje X":x,"Eje Theta":theta,"CL (alpha=0)":cl_T,"Cp (alpha = 0)":cp_T})
guardarcsv(cL_CT,"datoscl_solo_timon")
cl_total = cl_T + cl_ST

theta_a = arccos(2 * (xa - 0.5))  #  limite para la integral
alpha_char = np.array([-2, 0, 6])  #  angulos de ataque

C_CHAR_CT = np.array([])
C_CHAR_ST = np.array([])
c_char_CT_alpha = integrate.quad(coefcharnela, 0, theta_a, args=(theta_a, alpha_ST, CoefAN_ST + CoefAN_CT))[0]
for count, i in enumerate(alpha_char):
    c_CHAR_CT = integrate.quad(coefcharnela, 0, theta_a, args=(theta_a, np.radians(i), CoefAN_ST + CoefAN_CT))[0]
    c_CHAR_ST = integrate.quad(coefcharnela, 0, theta_a, args=(theta_a, np.radians(i), CoefAN_ST))[0]
    C_CHAR_CT = np.append(C_CHAR_CT, c_CHAR_CT)
    C_CHAR_ST = np.append(C_CHAR_ST, c_CHAR_ST)

coef_charnela = pd.DataFrame({"alpha": alpha_char, "M_CH_ST": C_CHAR_ST, "M_CH_CT": C_CHAR_CT})
guardarcsv(coef_charnela, "coeficientes_charnela")

numero_coefb0 = 200
nb0 = np.linspace(0,numero_coefb0,numero_coefb0+1)
Coefb0= (0.5 + (2/pi)*(integrate.quad(coefb0_0, 0, pi, args=(nb0,t))[0]) ) / ( (2/pi) * (integrate.quad(coefb0_1, 0, pi, args=(nb0))[0]) - 1 )
CoefBN = np.array([])
theta_bn = np.linspace(0,pi-0.001,100)
xbn = 0.5+cos(theta_bn)*0.5

for index, value in enumerate(nb0):
    if index == 0:
        continue
    else:
        coef1 = 2/pi * integrate.quad(coefBN , 0 , pi, args = (int(index),Coefb0))[0]
        CoefBN = np.append(CoefBN,coef1)
CoefBN = np.append(Coefb0,CoefBN)
COEFCIENTES_BN = pd.DataFrame({"B":nb0,"Valores":CoefBN})
guardarcsv(COEFCIENTES_BN,"coeficientes_bn")

cp_bn = -2*(CoefBN [0]-sumatorioBN(nb0,CoefBN,theta_bn))
cpe = cp_ST + cp_bn
cpi = -cp_ST + cp_bn
CP_ESPESOR = pd.DataFrame({"Eje X":xbn,"Eje Theta":theta_bn,"CP":cp_bn,"Cp_extrados":cpe,"Cp_intrados":cpi})
guardarcsv(CP_ESPESOR,"cp_espesor")
