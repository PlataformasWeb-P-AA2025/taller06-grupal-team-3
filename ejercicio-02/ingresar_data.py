import requests

from sqlalchemy.orm import sessionmaker

from generar_base import Pais
from generar_base import engine


Session = sessionmaker(bind=engine)
session = Session()

archivo = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')

datos_json = archivo.json()

for d in datos_json:
    print(d)
    print(len(d.keys()))
    p = Pais(nombre=d['CLDR display name'], 
             capital=d['Capital'], 
             continente=d['Continent'], 
             geoname_id = d['Geoname ID'],
             dial=d['Dial'], 
             itu=d['ITU'], 
             lenguajes=d['Languages'], 
             independiente=d['is_independent'])
    session.add(p)  
session.commit()