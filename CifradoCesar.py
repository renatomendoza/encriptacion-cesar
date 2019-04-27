
DESPL = 3
BASE = 65
FIN = 122 + 1

def encriptacion(texto):
	global DESPL
	nuevoTexto = ""
	for letra in texto:
		nuevoTexto += chr((ord(letra) + DESPL) % FIN)

	return nuevoTexto

	
def desencriptacion(texto):
	global DESPL
	nuevoTexto = ""
	for letra in texto:
		nuevoTexto += chr((ord(letra) - DESPL) % FIN)

	return nuevoTexto
	

if __name__ == '__main__':
	cadena = input("Ingresa una cadena: ")
	
	cadenaEnc = encriptacion(cadena)
	print("Encriptada: " + cadenaEnc)
	
	cadenaDes = desencriptacion(cadenaEnc)
	print("Desencriptada: " + cadenaDes)
