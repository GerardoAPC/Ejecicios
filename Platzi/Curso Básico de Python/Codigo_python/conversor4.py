def exchanges(moneda,cantidad):
    result = 0
    # Moneda chilena
    if moneda == 1:
        result = cantidad * 0.0013
        print(f'Los {cantidad} pesos chilenos equivalen a {result} dolares')
    # Moneda colombiana
    elif moneda == 2:
        result = cantidad * 0.00027
        print(f'Los {cantidad} pesos colombianos equivalen a {result} dolares')
    # Moneda Argentina
    elif moneda == 3:
        result = cantidad * 0.014
        print(f'Los {cantidad} pesos argentinos equivalen a {result} dolares')
    # Moneda mexicana
    elif moneda == 4:
        result = cantidad * 0.044
        print(f'Los {cantidad} pesos mexicanos equivalen a {result} dolares')
    # Otro
    else:
        print('Ingresa solo un numero de la lista')

def logica():
        punto_salida = 0
        while True:
                    try:
                        while True:
                            moneda = int(input('''
                            Ingresa el indice de la moneda que quieres convertira  dolar:
                                [1] Moneda chilena a Dolar
                                [2] Moneda colombiana a Dolar
                                [3] Moneda argentida a Dolar
                                [4] Moneda mexicana a Dolar
                                [0] Salir
                            Selecciona: '''))
                            print('********************************')
                            if(moneda >=0 and moneda <= 4):
                                break;

                        if(moneda == 0):
                            print('Bay bay')
                            punto_salida = 1
                        else:
                            cantidad = int(input('Ingresa la cantidad que quieres convertir: '))
                            exchanges(moneda,cantidad)
                    except:
                        print('Por favor, Ingresa solo valores numericos')
                    if(punto_salida == 1):
                        break;



if __name__ == '__main__':
    try:
        logica()
    except:
        logica()