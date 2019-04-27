import math

def calcular(num):
	arr = [1] * 1000000
	arr[0] = arr[1] = False
	for i in range(2, int(math.sqrt(num))+1):
		if arr[i] == True:
			j = i * i
			while j <= num:
				arr[j] = False
				j += i
	
	return arr


if __name__ == '__main__':
	primo = int(input("Ingrese un numero: "))
	arreglo = cribaEratostenes(primo)
	for i in range(primo+1):
		if arreglo[i] == True:
			print("Numero primo: ", i)
	
