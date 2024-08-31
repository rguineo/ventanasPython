# Esta seccion se importan los paquetes o librerias
from tkinter import *
#Funciones
def crearNuevo():
   # my_label = Label(root, text="Nuevo Documento de ejemplo").pack()
    print("Menu Archivo: Nuevo Documento")
    root.withdraw()
    ventanaNuevo.deiconify()

def guardar():
    print("Menu Archivo: Guardar Documento")
    root.withdraw()
    ventanaGuardar.deiconify()

def guardarComo():
    print("Menu Archivo: Guardar como ...")
    root.withdraw()
    ventanaGuardarComo.deiconify()

def menuPrincipal():
    ventanaNuevo.withdraw()
    ventanaGuardar.withdraw()
    ventanaGuardarComo.withdraw()
    root.deiconify()

root = Tk()
root.title("Menu Principal")
root.geometry("600x400")

my_menu = Menu(root)
root.config(menu=my_menu)

#Agregar opciones en el menu - Archivos
archivo_menu = Menu(my_menu)
my_menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Nuevo", command=crearNuevo)
archivo_menu.add_command(label="Guardar", command=guardar)
archivo_menu.add_command(label="Guardar como...", command=guardarComo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.quit)

# VENTANA Nuevo
ventanaNuevo = Tk()
ventanaNuevo.title("Nuevo Documento")
ventanaNuevo.geometry("600x400")
btnVolver = Button(ventanaNuevo, text="<< Menu Principal", command=menuPrincipal).pack()
ventanaNuevo.withdraw() #Ventana Oculta

# Ventana Guardar
ventanaGuardar = Tk()
ventanaGuardar.title("Guardar")
ventanaGuardar.geometry("600x400")
btnVolver = Button(ventanaGuardar, text="<< Menu Principal", command=menuPrincipal).pack()
ventanaGuardar.withdraw() #Ventana Oculta

# Ventana Guardar como
ventanaGuardarComo = Tk()
ventanaGuardarComo.title("Guardar como")
ventanaGuardarComo.geometry("600x400")
btnVolver = Button(ventanaGuardarComo, text="<< Menu Principal", command=menuPrincipal).pack()
ventanaGuardarComo.withdraw() #Ventana Oculta

root.mainloop()    