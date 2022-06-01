from neo4j import GraphDatabase

class Neo4jService(object):

    #Conexión a la base de datos 
    def __init__(self,uri,user,password):
        self._driver = GraphDatabase.driver(uri, auth=(user,password))

    def close(self):
        self._driver.close()

    #Crear un nodo Persona, que recibe como parámetro el nombre de la persona
    def crearPersona(self, tx, nombre):
        tx.run("CREATErsona {nombre: $nombre}", nombre = nombre)
    
    #Crear un nodo Club, que recibe como parámetro el nombre del club 
    def crearClub(self,tx,nombre):
        tx.run("CREATEclub {nombre: $nombre}", nombre = nombre)

    #Crear una relación entre Persona y Persona (amigos)
    def crearRelacionAmigos (self,tx, nombre1, nombre2):
        tx.run("MATCHersona {nombre: $nombre1}"
               "MATCH (b: Persona {nombre: $nombre2}"
               "MERGe (a) - [:FRIENDS] -> (b)",
               nombre1 =nombre1, nombre2 = nombre2)

    #Crear una relación entre Persona y Club (tipo de club)
    def crearRelacionClub (self,tx, nombrePersona, nombreClub ):
            tx.run("MATCHersona {nombre: $nombrePersona}"
                "MATCH (b: Persona {nombre: $nombreClub}"
                "MERGe (a) - [:TIPO] -> (b)",
                nombrePersona =nombrePersona, nombreClub = nombreClub)

    #Imprimir resultados
    def imprimirResultados(self,tx):
        result = tx.run("MATCH[:FRIENDS] -> (b) - [:TIPO] -> (c) RETURN a.nombre, b.nombre, c.nombre")
        for record in result:
            print("{} es amiga de {} y pertenece al club {}".format(record["a.name"], record["b.nome"], record["c.name"]))



