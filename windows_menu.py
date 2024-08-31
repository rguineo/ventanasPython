from tkinter import *

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
nuevo.withdraw() # ocultar ventana

# Creacion de ventana Guardar
guardar = Tk()
guardar.title("Guardar documento")
guardar.geometry("600x400")
btnReturn = Button(guardar, text="<< Regresar Menu Principal", command=backToMenu).pack()
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