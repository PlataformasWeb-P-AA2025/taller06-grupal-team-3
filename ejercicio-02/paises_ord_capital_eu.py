import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from generar_base import Pais, engine

Session = sessionmaker(bind=engine)
session = Session()

#filtra los paises que tengan como continente EU y los ordena por la capital
paises = session.query(Pais).filter(Pais.continente=="EU").order_by(Pais.capital).all()

print(paises)

for p in paises:
    print("Pais: %s - Capital: %s - Continente: %s" % (p.nombre, p.capital, p.continente))
    print("------------")

# Mostrar con Streamlit
st.title("Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa")

for p  in paises:
    st.write("Pais: %s - Capital: %s - Continente: %s" % (p.nombre, p.capital, p.continente))
    st.markdown("---")

st.markdown("---")
st.title("Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa en Tabla")
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