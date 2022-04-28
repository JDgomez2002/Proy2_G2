#Algoritmos y Estructura de Datos
#Catedrático Douglas Barrios
#Proyecto 2 Sistema de Recomendaciones
#Grupo 2
#Sofi Lam 21548
#Gabriela de León 21037
#Lourdes Saavedra 21333
#Daniel Gómez 21429

from pydoc import describe


def preferencia(num1):
    print()
    print("Preferencia "+str(num1))
    print("1. Deportes")
    print("2. Arte")
    myString = input("Ingrese su eleccion: ")
    print()
    if(myString=="1"):
        print("1. Deporte con contacto")
        print("2. Deporte sin contacto")
        deporte = input("Ingrese su eleccion: ")
        if(deporte=="1"):
            myString = "Club de Basketball\nClub de Football"
        else:
            myString = "Club de Ajedrez\nClub de Voleiball"
    else:
        print("1. Arte musical")
        print("2. Arte visual")
        arte = input("Ingrese su eleccion: ")
        if(arte=="1"):
            myString = "club de Marimba\nClub de Karaoke"
        else:
            myString = "Club de Fotografia\nClub de Dibujo"
    print("\nRecomendaciones:\n"+myString)

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
    print("\nTodas sus preferencias son:\n"+preferencia_1+"\n"+preferencia_2)
    print("-----------------------------------------------------------------")
    print()
    print("Espere un momento...")
    print("Analizando sus preferencias con neustra base de datos...")
    print()
    print("-----------------------------------------------------------------")
    print("-------------------------- Resultados! --------------------------")
    print("-----------------------------------------------------------------")
    print("Sus resultados son: ")
    print("-----------------------------------------------------------------")

    continuar = continuar_en_programa()

despedida()