import socket
import sys
import struct
import CifradoCesar as cifrado
import utils
from tkinter import *
from tkinter import scrolledtext
import server_socket

PORT = 8083

IP = "192.168.0.8"
BUFSIZE = 1024


def send_msg(sock, msg):
    msg = utils.charToAscii(msg)

    size_of_package = sys.getsizeof(msg)
    package = str(size_of_package) + ":" + msg

    sock.sendall(str.encode(package, 'ascii'))


def recv_msg(sock):
    header = sock.recv(2)
    header = header.decode('ascii')

    while ":" not in str(header):
        recibido = sock.recv(2)
        header += recibido.decode('ascii')

    size_of_package, separator, message_fragment = header.partition(":")
    message = sock.recv(int(size_of_package))
    message = message.decode('ascii')

    full_message = message_fragment + message
    full_message = utils.asciiToChar(full_message)
    return full_message


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((IP, PORT))
        try:
            ventana = Tk()
            ventana.title("Chat César - Cliente")

            labelClavesPublicas = Label(ventana, text = 'Claves publicas')
            labelMensaje = Label(ventana,text = 'Mensaje')
            labelInput = Label(ventana, text = 'Ingrese Mensaje')
            fieldText = Entry(ventana)

            fieldPublicas = scrolledtext.ScrolledText(ventana, height = 1, width = 15, font = "Arial")
            scrollText = scrolledtext.ScrolledText(ventana, height = 6, width = 33, font = "Arial")
            def setPublicas():    
                fieldPublicas.insert(INSERT, str(llaveCompartida))
            def clearFieldText():
                fieldText.delete(0, END)

            def cifrarTexto():
                mensaje =fieldText.get()
                mensajeCifrado = cifrado.encriptacion(mensaje)                         
                mensajeDescifrado = cifrado.desencriptacion(mensajeCifrado)
               #scrollText.insert(INSERT, 'Cifrado: '+cifrarTexto() +"\n")
                scrollText.insert(INSERT,'Cliente: ' +mensajeDescifrado+"\n")
                clearFieldText()
                return mensajeCifrado

            def enviarTexto():                        
                send_msg(s,cifrarTexto())
                
            def recibirTexto():
                textoCifrado = recv_msg(s)
                textoDescifrado = cifrado.desencriptacion(textoCifrado)
                scrollText.insert(INSERT, 'CifradoServidor: '+textoCifrado +'\n')
                scrollText.insert(INSERT,'DescifradoServidor: ' +textoDescifrado + "\n")

            buttonMostrar = Button (ventana, text = 'Mostrar', width =12, command = setPublicas)
            buttonEnviar = Button (ventana, text = 'Enviar', width =12, command = enviarTexto )
            buttonRecibir = Button (ventana, text = 'Recibir', width = 12, command = recibirTexto)
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
                buttonRecibir.grid(row = 10, column =4)
                ventana.mainloop()

            crearVentana()

            message = input("Client: ")
            messageCifrado =cifrado.encriptacion(message)
            send_msg(s, messageCifrado)
            textoCifrado = recv_msg(s)
            textoDescifrado = des.desencriptacion(textoCifrado)
            print("Server cifrado:", textoCifrado)
            print("Server mensaje: ", textoDescifrado)

        finally:
        	s.close()

    except OSError:
        print("# Socket already used")
        s.close()
