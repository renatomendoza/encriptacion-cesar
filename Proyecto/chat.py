from tkinter import *
from tkinter import scrolledtext
import cifradoDiffieHellman as cifrado
import cifradoDes as des
import server_socket

ventana = Tk()
ventana.title("Diffie Chat")

labelClavesPublicas = Label(ventana, text = 'Claves publicas')
labelMensaje = Label(ventana,text = 'Mensaje')
labelInput = Label(ventana, text = 'Ingrese Mensaje')

fieldText = Entry(ventana)

fieldPublicas = scrolledtext.ScrolledText(ventana, height = 1, width = 15, font = "Arial")
scrollText = scrolledtext.ScrolledText(ventana, height = 6, width = 33, font = "Arial")


def setPublicas(Mensaje):
	Mensaje = StringVar()
	fieldPublicas.insert(INSERT, Mensaje.get())


'''def getFieldText():
	return fieldText.get()
'''

def clearFieldText():
	fieldText.delete(0, END)


def setText():
	scrollText.insert(INSERT, fieldText.get() + "\n")
	clearFieldText()


buttonMostrar = Button (ventana, text = 'Mostrar', width =12, command = setPublicas)
buttonEnviar = Button (ventana, text = 'Enviar', width =12, command = setText)


def crearVentana():
	ventana.geometry('500x300')

	labelClavesPublicas.grid(row=0,column=0,columnspan=2)
	labelMensaje.grid(row = 3, column = 1, columnspan = 2)
	labelInput.grid(row = 10, column = 1, columnspan = 2)

	fieldText.grid(row = 11, column = 1, columnspan = 3)

	fieldPublicas.grid(row = 1, column = 1, columnspan = 3)
	scrollText.grid(row = 4,rowspan = 6, column = 1, columnspan = 3)

	buttonMostrar.grid(row = 1 , column = 4)
	buttonEnviar.grid(row = 11, column = 4)
	ventana.mainloop()

crearVentana()