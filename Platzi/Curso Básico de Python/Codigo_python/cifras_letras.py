def unidades(digito: int):
    numeros = ("", "UNO", "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE")
    return(numeros[digito])


def decenas(digitos: int):
    numeros = ("", "DIEZ", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA")
    nombres10 = ("", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE")
    cantidad = int(digitos) // 10
    resto = int(digitos) - cantidad * 10
    texto = ""
    if cantidad == 1 and resto > 0: #Los numeros de la primera decena tienen nombres específicos
        texto = nombres10[resto]
    else:
        texto = numeros[cantidad] 
        if resto > 0 :
            if cantidad > 0:
                texto += " Y " # Si hay decenas y unidades
            texto += unidades(resto) 
    return(texto.strip()) # Se devuelve el texto sin espacios en los extremos


def centenas(digitos: int):
    cantidad = int(digitos) // 100
    resto = int(digitos) - cantidad * 100
    texto = ""
    if cantidad > 0:
        if cantidad == 1:
            if resto == 0:
                texto = "CIEN"
            else:
                texto = "CIENTO"
        elif cantidad == 5:
            texto = "QUINIENTOS"
        elif cantidad == 7:
            texto = "SETECIENTOS"
        elif cantidad == 9:
            texto = "NOVECIENTOS"
        else:
            texto = unidades(cantidad) + "CIENTOS"
    texto += " " + decenas(resto)
    return(texto.strip()) # Se devuelve el texto sin espacios en los extremos


def millares(digitos: int):
    cantidad = int(digitos) // 1000
    resto = int(digitos) - cantidad * 1000
    texto = centenas(resto)
    if cantidad > 0:
        texto = "MIL " + texto
        if cantidad > 1: # evitar UNO MIL
            texto = centenas(cantidad) + " " + texto
    return(texto.strip()) # Se devuelve el texto sin espacios en los extremos


def millones(digitos: int):
    cantidad = int(digitos) // 1000000
    resto = int(digitos) - cantidad * 1000000
    texto = ""
    if cantidad == 1:
        texto = " MILLON "
    elif cantidad > 1:
        texto = " MILLONES "

    texto = millares(cantidad) + texto + millares(resto)
    return(texto.strip()) # Se devuelve el texto sin espacios en los extremos


def cifras_a_letras(digitos: float, moneda: str, fraccion_moneda: str):
    if digitos == 0:
        return("CERO")
    else:
        if digitos > 999999999999:
            return("Número demasiado grande")
        else:
            # Separa los enteros de los decimales para calcular el texto independientemente
            enteros = int(digitos)
            decimales = (digitos - enteros) * 100 // 1 # obtiene los dos primeros decimales como enteros (dedondea a 2)
            # Calcula el texto para enteros y decimales
            texto = millones(enteros) + " " + moneda
            if decimales > 0:
                texto += " CON " + decenas(decimales) + " " + fraccion_moneda
            return(texto)


def pruebas():
     test = (21.123, 0, 1, 3, 11, 12.256, 20, 21, 23, 32, 45, 50, 99, 100, 101, 123, 500, 501, 513, 1000, 1001, 11534126, 999999999999)
     for n in test:
         print((n, cifras_a_letras(n, "", "")))


def run():
    # pruebas()
    titulo = "\n\nIntroduzca un número:\n"
    texto = ""
    while True:
        numero = float(input(texto + titulo))
        texto = cifras_a_letras(numero, "$", "¢")
    

if __name__ == "__main__" :
    run()