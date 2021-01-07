# Aeroetsiae: Repositorio del trabajo de Aerodinámica NSA de 3º del Grado en Ingeniería Aeroespacial ETSIAE(UPM)
(En desarrollo / In development)
[ 🇪🇸 ](https://github.com/jaimebw/aeroetsiae/blob/master/README.md)             [ 🇬🇧 ](https://github.com/jaimebw/aeroetsiae/blob/master/README_eng.md)
## Introducción
Dentro de esta repo se encuentra una formulación de la teoría potencial linealizada para perfiles NACA de 4 cifras. La clase permite generar todo los datos, exportalos y representarlos.

## Instalación
Por ahora, solo tienes que descargarte la carpeta ```aerodynamics``` y ponerlo en tu directorio de trabajo.
Una vez hecho eso, poner esta frase en tu libro o script para exportar la clase:
```python
from aerodynamics.aero import airfoil
dni = "1234567"
perfil = airfoil(dni)
S
```
Se recomienda usar [Jupyter Lab/Books](https://www.anaconda.com/products/individual) 
## Calculo y funciones incluidas

Lo que cálcula este programa son:
- Los coeficientes de Glauert para el perfil sin/solo o con Timon
- Los coeficientes de sustentación y de presiones para el perfil sin/solo o con Timon
- Los coeficientes de charnela para el perfil sin o con Timon
- Los coeficientes Glauert para el espesor(B0,B1,...Bn)
- El coeficiente de presiones para el espesor, extrados e intrados

## Dependencias
Para poder usar el libro se necesitan instalar las librerias:
- Pandas( https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
- Numpy (https://docs.scipy.org/doc/numpy/user/install.html)
- Scipy (https://www.scipy.org/install.html)
- Matplotlib(solo el libro)(https://matplotlib.org/3.2.1/users/installing.html)

## Contribuciones
Este programa calcula lo necesario para poder hacer el trabajo, no obstante, si se quiere realizar alguna modificación o mejorar el código eres más que bienvenido a hacerlo. Haz una pull request o un fork y modificalo como quieras.
