import wikipedia
import os

cantidad = 0

def menu():
    os.system("clear")
    print('''
¡Hola! Bienvenido al conversor de monedas internacionales del Banco Central Platzi
Presiona la opción que quieres realizar: \n
1. Convertir de una moneda a otra
2. Información extra
3. Salir
        ''')

def menu_conversiones():
    os.system("clear")
    print('''
A que moneda quiere convertir? \n
1. Dolares -> Euros
2. Euros -> Dolares
3. Pesos dominicanos -> Dolares
4. Pesos dominicanos -> Euros
5. Dolares -> Pesos dominicanos
6. Euros -> Pesos dominicanos
7. Volver al menu principal
    ''')

def bucle_submenu():
    menu_conversiones()
    continuar = True
    while(continuar):
        opt = int(input("Digite el numero que acompañana a su opcion: "))
        if opt == 1:
            convertir_dolar_euro()
        elif opt == 2:
            os.system("clear")
            convertir_euro_dolar()
        elif opt == 3:
            os.system("clear")
            convertir_dom_dolares()
        elif opt == 4:
            os.system("clear")
            convertir_dom_euros()
        elif opt == 5:
            os.system("clear")
            convertir_dolar_dom()
        elif opt == 6:
            os.system("clear")
            convertir_euro_dom()
        elif opt == 7:
            os.system("clear")
            o = input("Realmente desea salir? s/n: ")
            if o == "n":
                bucle_menu()
            elif o == "s":
                bucle_menu()
            else:
                os.system("clear")
                input("Opcion no valida, presione enter y seleccione una opcion existente ")
                menu()
        else:
            os.system("clear")
            input("Opcion no valida, presione enter y seleccione una opcion existente ")
            menu()

def convertir_dolar_euro():
    os.system("clear")
    cantidad = float(input("Ingrese la cantidad de dolares: "))
    euro = 0.82
    resultado = float(cantidad*euro)
    resultado = round(resultado, 4)
    print(f"{cantidad} dolares son iguales a: {resultado} euros")
    input("Presione enter para volver al menu ")
    bucle_submenu()

def convertir_euro_dolar():
    cantidad = float(input("Ingrese la cantidad de euros: "))
    dolar = 1.22
    resultado = float(cantidad*dolar)
    resultado = round(resultado, 4)
    print(f"{cantidad} euros son iguales a: {resultado} dolares (estadounidenses)")
    input("Presione enter para volver al menu ")
    bucle_submenu()

def convertir_dom_dolares():
    cantidad = float(input("Ingrese la cantidad de pesos dominicanos: "))
    dolar = 0.017
    resultado = float(cantidad*dolar)
    resultado = round(resultado, 4)
    print(f"{cantidad} dominicanos son iguales a: {resultado} dolares (estadounidenses)")
    input("Presione enter para volver al menu ")
    bucle_submenu()

def convertir_dom_euros():
    cantidad = float(input("Ingrese la cantidad de pesos dominicanos: "))
    euro = 0.014
    resultado = float(cantidad*euro)
    resultado = round(resultado, 4)
    print(f"{cantidad} dominicanos son iguales a: {resultado} euros")
    input("Presione enter para volver al menu ")
    bucle_submenu()

def convertir_dolar_dom():
    cantidad = float(input("Ingrese la cantidad de dolares: "))
    dolar = 58.2
    resultado = float(cantidad*dolar)
    resultado = round(resultado, 4)
    print(f"{cantidad} dolares son iguales a: {resultado} pesos (dominicanos)")
    input("Presione enter para volver al menu ")
    bucle_submenu()

def convertir_euro_dom():
    cantidad = float(input("Ingrese la cantidad de euros: "))
    euro = 71.28
    resultado = float(cantidad*euro)
    os.system("clear")
    resultado = round(resultado, 4)
    print(f"{cantidad} euros son iguales a: {resultado} pesos (dominicanos)")
    input("Presione enter para volver al menu ")
    bucle_submenu()


def bucle_menu():
    menu()
    continuar = True
    while(continuar):
        opt = int(input("Digite el numero que acompañana a su opcion: "))
        if opt == 1:
            bucle_submenu()
        elif opt == 2:
            print(wikipedia.summary("Platzi", sentences=10))
            input("Presione enter para volver al menu")
            menu()
        elif opt == 3:
            o = input("Realmente desea salir? s/n: ")
            if o == "n":
                bucle_menu()
            elif o == "s":
                exit()
            else:
                input("Opcion no valida, presione enter y seleccione una opcion existente ")
                menu()
        else:
            input("Opcion no valida, presione enter y seleccione una opcion existente ")
            menu()

bucle_menu()