import tkinter as tk
from tkinter import ttk, Tk, Label, Button, messagebox, Menu, Entry
from database import selectDB, insertDB

# Variables
rows = []

# Funciones
def funcMenu():
    print("Menu Seleccionado")

def nuevoDoc():
    principal.withdraw() # ocultar ventana principal
    nuevo.deiconify() # mostrar ventana nuevo

def guardarDoc():
    principal.withdraw() # ocultar ventana principal
    guardar.deiconify() # mostrar ventana gurdar

def guardarDocComo():
    principal.withdraw() # ocultar ventana principal
    guardarComo.deiconify() # mostrar ventana gurdarComo

def backToMenu():
    nuevo.withdraw() # ocultar ventana nuevo
    guardar.withdraw() # ocultar ventana gurdar
    guardarComo.withdraw() # ocultar ventana gurdarComo
    
    principal.deiconify() #mostrar ventana principal

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

def findUsers():
    rows = selectDB()

    # Limpiar la tabla antes de mostrar nuevos datos
    for i in tree.get_children():
        tree.delete(i)

    print(rows)
    # Insertar cada fila en la tabla de tkinter
    for row in rows:
        tree.insert("", tk.END, values=row)

    
## Creacion de ventanas ##

# Creacion de ventana principal
principal = Tk()
principal.title("Menu Princpal")
principal.geometry("600x400")

# Creacion de ventana Nuevo documento
nuevo = Tk()
nuevo.title("Nuevo documento")
nuevo.geometry("600x400")
btnReturn = Button(nuevo, text="<< Regresar Menu Principal", command=backToMenu).pack()

# Los Labels son textos que hacen referencia una Caja de Texto
label1 = Label(nuevo, text="Nombre Usuario")
label1.place(relx=0.01, rely=0.15) 

# Place es la ubicacion en la ventana. relx, rely son posiciones relativas, es decir, posicion establecida a traves de un porcentaje.

input1 = Entry(nuevo) #Entry es un cuadro de texto o caja de texto
input1.place(relx=0.2, rely=0.15) 

label2 = Label(nuevo, text="Password")
label2.place(relx=0.01, rely=0.22)

input2 = Entry(nuevo)
input2.place(relx=0.2, rely=0.22)

label3 = Label(nuevo, text="Nombre")
label3.place(relx=0.01, rely=0.29)

input3 = Entry(nuevo)
input3.place(relx=0.2, rely=0.29)

label4 = Label(nuevo, text="Apellido")
label4.place(relx=0.01, rely=0.36)

input4 = Entry(nuevo)
input4.place(relx=0.2, rely=0.36)

btn = Button(nuevo, text="Guardar", command=funcBtnInsert) #Button es un boton para realizar acciones, el command hace un llamado a una funcion

btn.place(relx=0.55, rely=0.15, relwidth=0.15, relheight=0.12)

nuevo.withdraw() # ocultar ventana

# Creacion de ventana Guardar
guardar = Tk()
guardar.title("Guardar documento")
guardar.geometry("800x400")
btnReturn = Button(guardar, text="<< Regresar Menu Principal", command=backToMenu).pack()

## Agregar una tabla para los datos
tree = ttk.Treeview(guardar, columns=("Columna1", "Columna2", "Columna3", "Columna4"), show='headings')
tree.heading("Columna1", text="UserName")
tree.heading("Columna2", text="Password")
tree.heading("Columna3", text="Nombre")
tree.heading("Columna4", text="Apellido")

# Empaquetar el Treeview en la ventana
tree.pack(fill=tk.BOTH, expand=True)

# Botón para realizar la consulta
button = tk.Button(guardar, text="Consultar", command=findUsers).pack()
guardar.withdraw() # ocultar ventana

# Creacion de ventana Guardar como
guardarComo = Tk()
guardarComo.title("Guardar documento como")
guardarComo.geometry("600x400")
btnReturn = Button(guardarComo, text="<< Regresar Menu Principal", command=backToMenu).pack()
guardarComo.withdraw() # ocultar ventana

## Creacion del menu principal
my_menu = Menu(principal)
principal.config(menu=my_menu)

# Lista del menu archivo

archivo_menu = Menu(my_menu)
my_menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Nuevo", command=nuevoDoc)
archivo_menu.add_command(label="Guardar", command=guardarDoc)
archivo_menu.add_command(label="Guardar como", command=guardarDocComo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=principal.quit)

# Lista del menu editar
editar_menu = Menu(my_menu)
my_menu.add_cascade(label="Editar", menu=editar_menu)
editar_menu.add_command(label="Buscar", command=funcMenu)
editar_menu.add_command(label="Reemplazar", command=funcMenu)
editar_menu.add_separator()
editar_menu.add_command(label="Deshacer", command=funcMenu)
editar_menu.add_command(label="Rehacer", command=funcMenu)

# Lista del menu opciones
opciones_menu = Menu(my_menu)
my_menu.add_cascade(label="Opciones", menu=opciones_menu)
opciones_menu.add_command(label="Preferencias", command=funcMenu)
opciones_menu.add_command(label="Configuraciones", command=funcMenu)
opciones_menu.add_command(label="Idioma", command=funcMenu)
opciones_menu.add_separator()
opciones_menu.add_command(label="Acerca de", command=funcMenu)

principal.mainloop()