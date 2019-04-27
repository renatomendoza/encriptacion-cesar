

def charToAscii(cadena):
    # cadena = "Hola" => ascii = "72;111;108;97;"
    ascii = ""
    for val in cadena:
        ascii += str(ord(val)) + ';'
    return ascii


def asciiToChar(ascii):
    # ascii = "72;111;108;97;" => cadena = "Hola"
    lista = ascii.split(';')
    char = ""
    for val in lista:
        if val: char += chr(int(val))
    return char
