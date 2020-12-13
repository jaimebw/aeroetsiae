# Aeroetsiae: Repositorio del trabajo de Aerodinámica NSA de 3º del Grado en Ingeniería Aeroespacial ETSIAE(UPM)
## Funcionamiento del libro
Este repositorio contiene el trabajo de aerodinámica de la asignatura de AMV de la especialidad de NSA.  
Tiene el libro original con el que he hecho el trabajo yo. Su funcionamiento es sencillo: lo único que hay que hacer es sustituir los datos dentro de la primer celda del libro, y darle a ejecutar las celdas; acto seguido, se generará una carpeta llamada datos_csv que contedrá los csv que se pueden exportar a Excel.  
Lo que cálcula este programa son:
- Los coeficientes de Glauert para el perfil sin timón y SOLO el timón
- Los coeficientes de sustentación y de presiones para el perfil sin timón y SOLO el timón
- Los coeficientes de charnela para el perfil sin timón y para el perfil CON timón
- Los coeficientes Glauert para el espesor(B0,B1,...Bn)
- El coeficiente de presiones para el espesor, extrados e intrados
## Funcionamiento del ejecutable de Python
Se pone el DNI y se ejecuta, y acto seguido se generaran varios archivos .csv en una caperta con todos los datos anteriores.
## Dependencias
Para poder usar el libro se necesita instalar las librerias:
- Pandas( https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
- Numpy (https://docs.scipy.org/doc/numpy/user/install.html)
- Scipy (https://www.scipy.org/install.html)
- Matplotlib(solo el libro)(https://matplotlib.org/3.2.1/users/installing.html)

## Futuro
Estoy intentando crear archivo un ejecutable para Windows(.exe) para quien no sepa usar Python, y una página con la documentación para implementar esto cómo un paquete.
## Contribuciones
Este programa calcula lo necesario para poder hacer el trabajo, no obstante, si se quiere realizar alguna modificación o mejorar el código eres más que bienvenido a hacerlo. Haz una pull request o un fork y modificalo como quieras.
