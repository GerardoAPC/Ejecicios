
def conversacion (mensaje):
    print('Hola')
    print('Como estás?')
    print(mensaje)
    print('Adiós')


opcion = int(input('elige una opción: (1, 2, 3): '))
if opcion == 1:
    conversacion ('Eligiste la opcion 1')
elif opcion == 2:
    conversacion ('Eligiste la opcion 2')
elif opcion == 3:
    conversacion ('Eligiste la opcion 3')
else:
    print('Escribe una opción correcta')