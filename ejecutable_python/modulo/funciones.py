import numpy as np
import os
from numpy import cos, sin, arccos, pi,tan
import scipy.integrate as integrate
import pandas as pd


def coefA0(xf, f):
    # Coeficiente A0 para el perfil sin timon
    lim_inf = 0
    lim_sup = pi
    lim_medio = medio = arccos([(xf - 0.5) * 2])[0]
    tramo1 = integrate.quad(lambda x: f / (1 - xf) ** 2 * (2 * xf - 1 - cos(x)), lim_inf, lim_medio)
    tramo2 = integrate.quad(lambda x: f / xf ** 2 * (2 * xf - 1 - cos(x)), lim_medio, lim_sup)

    return -1 / pi * (tramo1[0] + tramo2[0])

def coefAN(n, xf, f):
    # Coeficientes AN para el perfil sin timon
    lim_inf = 0
    lim_sup = pi
    lim_medio = medio = arccos([(xf - 0.5) * 2])[0]
    tramo1 = integrate.quad(lambda x: (f / (1 - xf) ** 2 * (2 * xf - 1 - cos(x))) * cos(n * x), lim_inf, lim_medio)
    tramo2 = integrate.quad(lambda x: (f / xf ** 2 * (2 * xf - 1 - cos(x))) * cos(n * x), lim_medio, lim_sup)

    return -2 / pi * (tramo1[0] + tramo2[0])

def coefA0_T(ca, delta_a):
    # Coeficiente A0 para el perfil con timon
    lim_inf = 0
    lim_medio2 = arccos([((1 - ca) - 0.5) * 2])[0]
    tramo1 = integrate.quad(lambda x: tan(delta_a), lim_inf, lim_medio2)
    return -1 / pi * tramo1[0]

def coefAN_T(ca, delta_a, n):
    # Coeficiente A0 para el perfil con timon
    lim_inf = 0
    lim_medio2 = arccos([((1 - ca) - 0.5) * 2])[0]
    tramo1 = integrate.quad(lambda x: tan(delta_a) * cos(n * x), lim_inf, lim_medio2)
    return -2 / pi * tramo1[0]

def sumAN(theta, CoefAN, n):
    Sumatorio = np.array([])

    for count, i in enumerate(theta):

        sumatorio = 0

        for count2, j in enumerate(n):
            if count2 == 0:
                continue
            else:
                sumatorio += CoefAN[count2] * sin(int(count2) * i)
        Sumatorio = np.append(Sumatorio, sumatorio)
    return Sumatorio

def coefcharnela(theta, theta_a, alpha, A):
    # todos los ángulos tiene que ser puesto en radianes
    sum = 0
    # get sum
    for index, value in enumerate(A):
        if index == 0:
            sum += (alpha + A[index]) * tan(0.5 * theta)
        else:
            sum += A[index] * sin(index * theta)
    # note that multiplication with 4 and multiplication with 1/4
    # result in one as prefactor
    return -sum * (cos(theta) - cos(theta_a))*sin(theta)

def coefb0_0(theta, n, t):
    # calcula el primer cacho del coeficiente B0(integral del numerador)
    a = 0.2969
    b = -0.126
    c = -0.3516
    d = 0.2843
    e = -0.1015
    cv = 0.5+0.5*cos(theta)
    sum = 0
    # get sum
    for index, value in enumerate(n):
        if index == 0:
            continue
        else:
            sum += (5*t*( a/(2*(cv**0.5)) + b + 2*c*cv + 3*d*cv**2 + 4*e*cv**3)) * sin(index * theta) * cos(index*pi)
    return sum

def coefb0_1(theta,n):
    # calcula el segundo cacho del coeficiente B0(integral del denominador)
    sum2 = 0
    for index, value in enumerate(n):
        if index == 0:
            continue
        else:
            sum2 += tan(theta*0.5)*sin(index*theta)*cos(index*pi)
    return sum2

def coefBN(theta,n,b0):
    # calcula el coeficiente BN
    a = 0.2969
    b = -0.126
    c = -0.3516
    d = 0.2843
    e = -0.1015
    t = 0.12
    cv = 0.5+0.5*cos(theta)
    d_esp = (5*t*( a/(2*(cv**0.5)) + b + 2*c*cv + 3*d*cv**2 + 4*e*cv**3))
    return (d_esp - b0*tan(theta*0.5))*sin(theta*n)

def sumatorioBN(n,BN,x):
    # segundo miembro del cp para el espesor
    #theta = arccos(2*(x-0.5))
    Sumatorio = np.array([])
    for count,i in enumerate(x):
        sumatorio = 0
        for count2,j in enumerate(n):
            if count2 == 0:
                continue
            else :
                sumatorio -= BN[count2]*cos(int(count2)*i)
        Sumatorio = np.append(Sumatorio,sumatorio)
    return Sumatorio

def guardarcsv(archivo, nombre_archivo):
    # guarda el archivo .csv en la carpeta especificada
    carpeta_datos_csv = r"datos_csv/"
    archivo.to_csv(carpeta_datos_csv+nombre_archivo+".csv")


def perfilnaca(DNI):
    # genera los parámetros del perfil
    """
    123VWXYZ
    01234567
    """
    try:
        f = 1 + int(int(DNI[3])*5/8)
        xf = 20 + 10*int(int(DNI[4])/8*2)
        t = 8 +int(int(DNI[5])*10/9)
        ca = 20 +5*int(int(DNI[6])*3/8)
        delta_a = 5 + 5*int(int(DNI[7])*2/8)
        parametros = np.array([f,xf,t,ca,delta_a])/100
        print("Tu perfil NACA es el",str(f),str(xf)[0],str(t))
        return parametros
    except :
        print("Error ")

