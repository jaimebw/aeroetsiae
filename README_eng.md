# Aeroetsiae:Repository with the airfoil theory for the uni Aeroespacial ETSIAE(UPM)
[ 🇪🇸 ](https://github.com/jaimebw/aeroetsiae/blob/master/README.md)             [ 🇬🇧 ](https://github.com/jaimebw/aeroetsiae/blob/master/README_eng.md)
## Introducction

This repo has a implementation of linealize potenthial teorhy for 4 digits NACA airfoils.

## Installation
At the moment, you have to download the folder ```aerodynamics```  and add it to your working dir.
Once that is done, you shall write the next code:
```python
from aerodynamics.aero import airfoil
dni = "1234567"
perfil = airfoil(dni)
S
```
It is recommeneded using [Jupyter Lab/Books](https://www.anaconda.com/products/individual) 
## Possible calculations with this library

- Glauert coeficientes for the airfoil with 
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
