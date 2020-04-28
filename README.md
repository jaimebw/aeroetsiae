# Aeroetsiae: Repositorio del trabajo de Aerodinámica
## Funcionamiento
Este repositorio contiene el trabajo de aerodinámica de la asignatura de AMV de la especialidad de NSA.  
Actualmente solo tiene el libro original con el que he hecho el trabajo yo, pero su funcionamiento es sencillo. Lo único que hay que hacer es sustituir los datos dentro de la primer celda del libro, y darle a ejecutar las celdas. Acto seguido, se generará una carpeta llamada datos_csv que contedrá los csv que se pueden exportar a Excel.  
Lo que cálcula este programa son:
- Los coeficientes de Glauert para el perfil sin timón y SOLO el timón
- Los coeficientes de sustentación y de presiones para el perfil sin timón y SOLO el timón
- Los coeficientes de Charnela para el perfil sin timón y para el perfil CON timón
- Los coeficientes Glauert para el espesor(B0,B1,...Bn)
- El coeficiente de presiones para el espesor, extrados e intrados

## Dependencias
Para poder usar el libro se necesita instalar las librerias:
- Pandas( https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
- Numpy (https://docs.scipy.org/doc/numpy/user/install.html)
- Scipy (https://www.scipy.org/install.html)
