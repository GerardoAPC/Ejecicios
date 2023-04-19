def conversor(tipo_pesos,valor_dolar):
	#pregunto al usuario la cantidad a convertir
	pesos = input('¿Cuántos pesos ' + tipo_pesos  + 'tienes?: ')
	#convierto a float para mejor manejo de datos
	pesos = float(pesos)
	#hago la conversión
	dolares = pesos / valor_dolar
	#redondeo los dólares a dos decimales
	dolares = round(dolares, 2)
	#convierto el float de dolares a un string
	dolares = str(dolares)
	#escribo el valor del dolar en pesos mexicanos
	print ("tienes $"+ dolares + "Dolares")



#convierte pesos mexicanos, argentinos y colombianos a dólares

# """ """ permite crear strings multilineas
menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos

Elige una opción: 

"""
# de derecha a izquierda: llamo a la funcion input, le paso la variable menu para que la imprima y reciba el número que el usuario escogió, lo convierto a int y lo guardo en la variable 'opcion'
opcion = int(input(menu))

if opcion == 1: #pesos mexicanos
	conversor ("Colombianos",3875)
elif opcion == 2: #pesos colombianos
	conversor ("Argentino",65)
elif opcion == 3: #pesos argentinos
	conversor ("Maxicanos",24)
else:  #el usuario escribió algo diferente
	print('Escribe una opción correcta: ')


