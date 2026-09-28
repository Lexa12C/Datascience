import os
import pandas as pd
from sqlalchemy import create_engine

DATABASE = "fifaworldcup"
CARPETA = r"C:\Users\Usuario\Documents\DataSci\datos\csvsubir"

engine = create_engine(f"mysql+pymysql://root:@localhost:3306/{DATABASE}")

for archivo in os.listdir(CARPETA):
    if archivo.lower().endswith(".csv"):
        tabla = os.path.splitext(archivo)[0].lower()
        df = pd.read_csv(os.path.join(CARPETA, archivo), sep=";", encoding="utf-8-sig")
        df.to_sql(tabla, engine, if_exists="replace", index=False)
        print(tabla, len(df))
        
        