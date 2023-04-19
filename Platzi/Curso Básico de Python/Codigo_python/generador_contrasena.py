import random


def generar_contrasena():
    #declaracion de listas
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos   = ['!', '#', '$', '&', '/', '(', ')']
    numeros    = ['0','1','2','3','4','5','6', '7', '8', '9']

    #declaracion de variables
    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []
    contador = 0

    #ciclo para generar contrasenas
    for i in range (15):
        caracter = random.choice(caracteres)
        contrasena.append(caracter)

    #conversion de lista a cadena de texto
    contrasena = "".join(contrasena)
    return contrasena   

    

def run():
    contrasena =  generar_contrasena()
    print('Tu nueva contrasena es: ' + contrasena)


if __name__ == "__main__":
    run()