# Datascience

Repositorio de entregas del curso de introducción a Data Science (ACM UD).

## Integrantes
- Argenis Alexandra Daza Roa

## Descripción del proyecto
Entrega 1: base de datos relacional en MySQL con los datos de la FIFA World Cup. Los CSV se limpian con Power Query, se cargan con Python a un esquema plano (`fifaworldcup`) y luego un script SQL construye el esquema normalizado (`fifaworldcup_normalized`) con 15 tablas, claves primarias, claves foráneas e integridad referencial.

## Tecnologías utilizadas
- MySQL (XAMPP) y phpMyAdmin
- Python, Pandas, SQLAlchemy, PyMySQL, Streamlit
- Power Query (Excel)
- LaTeX (informe)

## Cómo ejecutar la base de datos
1. Abrir XAMPP e iniciar **Apache** y **MySQL**.
2. Entrar a phpMyAdmin y crear una base de datos vacía llamada `fifaworldcup`.
3. Ejecutar primero los scripts de carga (sección siguiente).
4. En phpMyAdmin, abrir la pestaña **SQL**, pegar el contenido de `codigoPK_FK.txt` y ejecutar. Esto crea `fifaworldcup_normalized` con las 15 tablas.

## Cómo ejecutar los scripts de carga
1. Instalar las dependencias:
```bash
   pip install pandas sqlalchemy pymysql streamlit
```
2. En `1_cargarcsv.py`, cambiar la variable `CARPETA` por la ruta local de la carpeta con los CSV limpios.
3. Ejecutar:
```bash
   python 1_cargarcsv.py
```
   Al terminar imprime cada tabla con su número de filas cargadas.

## Informe
Ver `entrega1datascience.pdf`.
