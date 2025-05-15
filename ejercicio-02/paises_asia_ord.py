import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from generar_base import Pais, engine

Session = sessionmaker(bind=engine)
session = Session()

#filtra los paises que tengan el continente con la abreviatura AS y los ordena por el dia que es un numero
paises = session.query(Pais).filter(Pais.continente=="AS").order_by(Pais.dial).all()

print(paises)

for p in paises:
    print("Pais: %s - Continente: %s - Dial: %s" % (p.nombre, p.continente, p.dial))
    print("------------")


# Mostrar con Streamlit
st.title("Presentar los países de Asía, ordenados por el atributo Dial")

for p  in paises:
    st.write("Pais: %s - Continente: %s - Dial: %s" % (p.nombre, p.continente, p.dial))
    st.markdown("---")

st.markdown("---")
st.title("Presentar los países de Asía, ordenados por el atributo Dial en Tabla")
lista = []

for p in paises:
    diccionario = {"nombre":p.nombre, 
             "capital":p.capital, 
             "continente":p.continente, 
             "geoname_id":p.geoname_id,
             # se transforma el dial de integer a str para poder mostrar datos en caso de que no haya o valores invalidos
             "dial":str(p.dial), 
             "itu":p.itu, 
             "lenguajes":p.lenguajes, 
             "independiente":p.independiente}
    lista.append(diccionario)

st.dataframe(lista)