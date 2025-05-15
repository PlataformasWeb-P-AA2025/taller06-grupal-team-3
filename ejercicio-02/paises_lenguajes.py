import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from generar_base import Pais, engine

Session = sessionmaker(bind=engine)
session = Session()

#obtiene todos los paises
paises = session.query(Pais).all()

print(paises)

for p in paises:
    print("Pais:%s; Lenguajes: %s" % (p.nombre,p.lenguajes))
    print("------------")


# Mostrar con Streamlit
st.title("Presentar los lenguajes de cada país")

for p  in paises:
    st.write("Pais: %s - Lenguajes: %s" % (p.nombre, p.lenguajes))
    st.markdown("---")

st.markdown("---")
st.title("Presentar los lenguajes de cada país en Tabla")
lista = []

for p in paises:
    diccionario = {"nombre":p.nombre, 
             "capital":p.capital,
             "lenguajes":p.lenguajes}
    lista.append(diccionario)

st.dataframe(lista)