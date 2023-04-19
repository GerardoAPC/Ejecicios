def revisar_si_es_palindromo(palabra_o_frase):
    palabra_o_frase = palabra_o_frase.replace(" ", "")
    palabra_o_frase = palabra_o_frase.lower()
    counter = 0
    for i in range(len(palabra_o_frase)-1,-1,-1):
        caracteres_invertidos = palabra_o_frase[i]
        caracter = palabra_o_frase[abs(i-(len(palabra_o_frase)-1))]
        if caracter == caracteres_invertidos:
            counter += 1
        else:
            return False
    if counter == len(palabra_o_frase):
        return True

def run():
    palabra = input("Escribe una palabra o frase: ")
    es_palindromo = revisar_si_es_palindromo(palabra)
    if es_palindromo:
        print(palabra + " Es palindromo")
    else:
        print(palabra + " no es un palindromo")


# punto de entrada del programa


if __name__ == '__main__':
    run()

#Test case:
#revisar_si_es_palindromo("Luz Azul")
