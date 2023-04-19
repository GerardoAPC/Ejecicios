# Programa para aplicar todos los métodos para texto.

def metodos_string():
    print("")
    print("""
    Bienvenido, este es un resumen de aplicación para métodos de strings en python, 
    por favor escribe tu nombres y apellidos según te indique la consola:
    """)
    nombre = input("Escribe tu(s) nombre(s): ")
    apellido = input("Escribe tu(s) apellido(s): ")
    print("")
    nombre = nombre + " " + apellido
    print("El nombre que ingresaste es " + nombre)
    print("""
    A continuación aplicaremos todos los métodos de strings para tu nombre:
    """)
    print("Aplicando el método  UPPER  tenemos como resultado...nombre.upper() >>> " + nombre.upper())
    nombre = nombre.upper()
    print("Aplicando el método  LOWER  tenemos como resultado...nombre.lower() >>> " + nombre.lower())
    nombre = nombre.lower()
    print("Aplicando el método  CAPITALIZE  tenemos como resultado...nombre.capitalize() >>> " + nombre.capitalize())
    nombre = nombre.capitalize()
    print("Aplicando el método  TITLE  tenemos como resultado...nombre.title() >>> " + nombre.title())
    nombre = nombre.title()
    print("Aplicando el método  STRIP  tenemos como resultado...nombre.strip() >>> " + nombre.strip())
    nombre = nombre.strip()
    print("Aplicando el método  REPLACE  tenemos como resultado...nombre.replace('a','o') >>> " + nombre.replace("a", "o"))
    nombre = nombre.replace("a","o")
    print("")
    print("El resultado final de tu nombre es " + nombre + ", por cierto la longitud de caracteres que tiene tu nombre es de ---> " + str(len(nombre)) + " <--- caracteres")
    print("")

metodos_string()