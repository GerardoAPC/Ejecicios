def potencia(LIMITE):
    for contador in range(LIMITE+1):
        potencia_2 = 2**contador
        print(f'2 elevado a {contador} es igual a: {potencia_2}')


def tablasMultiplicar(tabla):
    for i in range(1,11):
        print(f' {i} por {tabla} = {i * tabla}')


def run():
    menu = input(""" 
        BIENVENIDO AL MENU DE PROGRAMAS
        1. Potencia de un numero.
        2. Tablas de multiplicar.

        Escoja una opción: 
        """)
    
    opcion = int(menu)
    if opcion == 1:
        LIMITE = int(input('Ingresa el limite: '))
        potencia(LIMITE)
    
    elif opcion == 2:
        tabla = int(input('Digite la tabla a multiplicar: '))
        tablasMultiplicar(tabla)
    
    else:
        print('Opcion no valida')


if __name__ == "__main__":
    run()