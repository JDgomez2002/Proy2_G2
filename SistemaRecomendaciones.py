#Algoritmos y Estructura de Datos
#Catedrático Douglas Barrios
#Proyecto 2 Sistema de Recomendaciones
#Grupo 2
#Sofi Lam 21548
#Gabriela de León 21037
#Lourdes Saavedra 21333
#Daniel Gómez 21429

from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","1234"))

#inicializacion d ebase de datos
def __init__(self, url, user, password):
    self.__url = url
    self.__user = user
    self.__pwd = password
    self.__driver = None
    try:
        self.driver = GraphDatabase.driver(self.__url, auth=(self.__user, self.__pwd))
    except Exception as e:
        print("Falla al crear Driver: ",e)

#cierre de la base de datos
def close(self):
    self.driver.close()

def preferencia(num1):
    print()
    print("Preferencia "+str(num1))
    print("1. Deportes")
    print("2. Arte")
    print("3. Ciencia")
    print("4. Agregar categoria de clubes")
    myString = input("Ingrese su eleccion: ")
    print()
    if(myString=="1"):
        print("1. Deporte con contacto")
        print("2. Deporte sin contacto")
        deporte = input("Ingrese su eleccion: ")
        if(deporte=="1"):
            print("\n1. Club de Basketball\n2. Club de Football")
            myString = input("Ingrese su desicion: ")
            if(myString=="1"):
                myString = "Club de Basketball"
            else:
                myString = "Club de Football"
        else:
            print("\n1. Club de Ajedrez\n2. Club de Voleiball")
            myString = input("Ingrese su desicion: ")
            if(myString=="1"):
                myString = "Club de Ajedrez"
            else:
                myString = "Club de Voleiball"
    elif(myString=="2"):
        print("1. Arte musical")
        print("2. Arte visual")
        arte = input("Ingrese su eleccion: ")
        if(arte=="1"):
            print("\n1. Club de Marimba\n2. Club de Karaoke")
            myString = input("Ingrese su desicion: ")
            if(myString=="1"):
                myString = "Club de Marimba"
            else:
                myString = "Club de Karaoke"
        else:
            print("\n1. Club de Fotografia\n2. Club de Dibujo")
            myString = input("Ingrese su desicion: ")
            if(myString=="1"):
                myString = "Club de Fotografia"
            else:
                myString = "Club de Dibujo"
    elif(myString=="3"):
        print("1. STEAM")
        print("2. Astronomia")
        arte = input("Ingrese su desicion: ")
        if(arte=="1"):
            myString = "Club de STEAM"
        else:
            myString = "Club de Astronomia"

    else:
        # print("Ingrese el nombre de la categoria de club: ")
    
        categoria = input("Ingrese el nombre de la categoria de club: ")
        print("\nCategoria de "+categoria+" creada exitosamente!")
        myString = "Clun de "+categoria

    return myString

def continuar_en_programa():
    print()
    myString = input("Desea finalizar el programa? (Si/No): ")
    myString = myString.lower()
    if(myString=="si"):
        return False
    else:
        return True
    print()

def despedida():
    print()
    print("-----------------------------------------------------------------")
    print("Muchas gracias por utilizar nuestro sistema de recomendacion!")
    print("Vuelve pronto!")
    print("-----------------------------------------------------------------")
    print()

continuar = True

while(continuar):
    print()
    print("-----------------------------------------------------------------")
    print("--------- Bienvenido al sistema de recomendaciones! -------------")
    print("-----------------------------------------------------------------")
    print("Aqui podras obtener recomendaciones de amistad segun tus\nactividades preferidas!")
    print("Utilizaremos tus preferencias en clubes universitarios!")
    print("-----------------------------------------------------------------")
    nombre_usuario = input("Ingrese su nombre: ")
    print()
    print("Bienvenido "+nombre_usuario+"!")
    print()
    print("-----------------------------------------------------------------")
    print("---------------- Eleccion de preferencias... --------------------")
    print("-----------------------------------------------------------------")

    preferencia_1 = preferencia(1);
    preferencia_2 = preferencia(2);

    print("-----------------------------------------------------------------")
    print("\nTodas sus preferencias son:\n1. "+preferencia_1+"\n2. "+preferencia_2+"\n")
    print("-----------------------------------------------------------------")
    print()
    print("Espere un momento...")
    print("Analizando sus preferencias con neustra base de datos...")
    print()
    print("-----------------------------------------------------------------")
    print("-------------------------- Resultados! --------------------------")
    print("-----------------------------------------------------------------")
    print("Sus resultados son: ")
    print("1. Miguel: Club de Basketball")
    print("2. Maria: Club de Marimba")
    print("3. Sofia: Amiga de Maria")
    print("-----------------------------------------------------------------")

    continuar = continuar_en_programa()

despedida()