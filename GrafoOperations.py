#Algoritmos y Estructura de Datos
#Catedrático Douglas Barrios
#Proyecto 2 Sistema de Recomendaciones
#Grupo 2
#Sofi Lam 21548
#Gabriela de León 21037
#Lourdes Saavedra 21333
#Daniel Gómez 21429

# from neomodel import config 

from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo)

config.DATABASE_URL = 'bolt://neo4j:neo4j@localhost:7687/Proyecto2G2'

class Club(StructuredNode):
    code = StringProperty(unique_index=True, required=True)

class Persona(StructuredNode):
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

#Crear una asociacion a la clase club
# myClub = RelationshipTo(Club, 'Asiste a')

#Operaciones con nodos
#Crear nodos
daniel = Persona(name='Daniel',age=19).save()
lou = Persona(name='Lourdes',age=20).save()
gaby = Persona(name='Gabriela',age=18).save()
sofi = Persona(name='Sofia',age=18).save()

miPersona = Persona.nodes.get_or_none(name='Daniel')

print(miPersona.get(name='Daniel'))