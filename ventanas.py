# Esta seccion se importan los paquetes o librerias
from tkinter import Tk, Button, Entry, Label, messagebox, Menu
from database import insertDB

## Insertamos un cambio para testear github


def funcBtnInsert():
    username = input1.get() 
    password = input2.get()
    firstName = input3.get()
    lastName = input4.get()

    insertDB(username, password, firstName, lastName)

    input1.delete(0, 'end')
    input2.delete(0, 'end')
    input3.delete(0, 'end')
    input4.delete(0, 'end')

# Se crea una ventana de interface para que el usuario ingre su informacion de registro de usuarios
ventana = Tk()
ventana.title("AIEP 2024") # Titulo de la ventana
ventana.geometry("600x480") # Dimensiones en pixeles

# Los Labels son textos que hacen referencia una Caja de Texto
label1 = Label(ventana, text="Nombre Usuario")
label1.place(relx=0.01, rely=0.05) 

# Place es la ubicacion en la ventana. relx, rely son posiciones relativas, es decir, posicion establecida a traves de un porcentaje.

input1 = Entry(ventana) #Entry es un cuadro de texto o caja de texto
input1.place(relx=0.2, rely=0.05) 

label2 = Label(ventana, text="Password")
label2.place(relx=0.01, rely=0.12)

input2 = Entry(ventana)
input2.place(relx=0.2, rely=0.12)

label3 = Label(ventana, text="Nombre")
label3.place(relx=0.01, rely=0.19)

input3 = Entry(ventana)
input3.place(relx=0.2, rely=0.19)

label4 = Label(ventana, text="Apellido")
label4.place(relx=0.01, rely=0.26)

input4 = Entry(ventana)
input4.place(relx=0.2, rely=0.26)

btn = Button(ventana, text="Guardar", command=funcBtnInsert) #Button es un boton para realizar acciones, el command hace un llamado a una funcion

btn.place(relx=0.55, rely=0.05, relwidth=0.15, relheight=0.12)

