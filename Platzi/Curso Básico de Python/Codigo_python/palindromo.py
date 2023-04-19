def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_alreves = palabra[::-1]
    if palabra == palabra_alreves:
        return True
    else:
        return False    

def run():
    palabra = input("Escribe una palabra: ")
    palabra_palindromo = palindromo(palabra)
    if palabra_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    run()