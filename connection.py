import streamlit as st
from sqlalchemy import create_engine

USER = "root"
PASSWORD = ""
HOST = "localhost"
PORT = 3306
DATABASE = "fifaworldcup"

@st.cache_resource
def get_connection_engine():
    """Crea y cachea el motor de conexión a la base de datos de MYSQL"""
    connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    engine = create_engine(connection_string)
    return engine


