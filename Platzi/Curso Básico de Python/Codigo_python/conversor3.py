def Wellcome():
    print("bienvenidos al conversor de monedas ")
    conmand = input("""
        elige la moneda que quieres convertir
        [1] pesos mexicanos
        [2] soles peruanos 
    """)

    return conmand

def Conversion(string):
    questing = input("""
        elige la forma de conversion
        [1] De dolares a {}
        [2] De {} a dolares
    """.format(string, string)
    )

    return questing

def run(money, dolar, questing, string ):
    if questing == "1":
        Dolares = int(input("cuantos Dolares quieres convertir a {}: ".format(string)))
        resultado = round(Dolares * money, 2)
        print("el resuldato de la conversion serian de {} {}".format(resultado, string))

    elif questing == "2":
        moneda = int(input("cuantos {} quieres convertir a Dolares: ".format(string)))
        resultado = round(dolar * moneda, 2)
        print("el resuldato de la conversion serian de {} Dolares".format(resultado))

if __name__ == "__main__":
    conmand = Wellcome() 

    if conmand == "1":
        pesos_me = 22.42
        dolar = 0.044
        questing = Conversion("pesos mexicanos")
        run(pesos_me, dolar, questing, "pesos mexicanos" )

    elif conmand == "2":
        soles_pe = 3.54
        dolar = 0.28
        questing = Conversion("soles peruanos")
        run(soles_pe, dolar, questing, "soles peruanos")
    
    else:
        print("___ERROR___\n \n intente colocando un numero por favor")```