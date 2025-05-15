import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from generar_base import Pais, engine

Session = sessionmaker(bind=engine)
session = Session()

#Filtra los paises que tengan como continente la abreviatura NA de norte-america y SA de sur-america
paises = session.query(Pais).filter(and_(Pais.continente=="NA", Pais.continente=="SA")).all()

print(paises)

for p in paises:
    print("Pais: %s - Continente: %s" % (p.nombre, p.continente))
    print("------------")


# Mostrar con Streamlit
st.title("Presentar todos los países del continente americano")

for p  in paises:
    st.write("Pais: %s - Continente: %s" % (p.nombre, p.continente))
    st.markdown("---")

st.markdown("---")
st.title("Presentar todos los países del continente americano en Tabla")
lista = []

for p in paises:
    diccionario = {"nombre":p.nombre, 
             "capital":p.capital, 
             "continente":p.continente, 
             "geoname_id":p.geoname_id,
             "dial":str(p.dial), 
             "itu":p.itu, 
             "lenguajes":p.lenguajes, 
             "independiente":p.independiente}
    lista.append(diccionario)

st.dataframe(lista)