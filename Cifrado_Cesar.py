def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo)
        else:
            resultado += caracter
    return resultado


def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo = (ord(caracter) - base - desplazamiento) % 26 + base
            resultado += chr(nuevo)
        else:
            resultado += caracter
    return resultado


# Programa principal
if __name__ == "__main__":
    print("=== Cifrado César ===")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    opcion = input("Seleccione una opción (1/2): ")

    if opcion == "1":
        texto = input("Ingrese el texto a cifrar: ")
        desplazamiento = int(input("Ingrese la cantidad de caracteres desplazados: "))
        texto_cifrado = cifrar_cesar(texto, desplazamiento)
        print("\nTexto cifrado:", texto_cifrado)

    elif opcion == "2":
        texto = input("Ingrese el texto cifrado: ")
        desplazamiento = int(input("Ingrese la cantidad de caracteres desplazados: "))
        texto_descifrado = descifrar_cesar(texto, desplazamiento)
        print("\nTexto descifrado:", texto_descifrado)

    else:
        print("Opción inválida. Intente nuevamente.")
