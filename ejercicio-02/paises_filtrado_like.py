import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from generar_base import Pais, engine

Session = sessionmaker(bind=engine)
session = Session()

#filtra los paises que tengan en su nombre uador o ito en su capital
paises = session.query(Pais).filter(or_(Pais.nombre.like("%uador"), Pais.capital.like("%ito"))).all()

print(paises)

for p in paises:
    print("Pais: %s" % (p.nombre))
    print("------------")

# Mostrar con Streamlit
st.title("Presentar todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito'")

for p  in paises:
    st.write("Pais: %s" % (p.nombre))
    st.markdown("---")

st.markdown("---")
st.title("Presentar todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito' en Tabla")
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
