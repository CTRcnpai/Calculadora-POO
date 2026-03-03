# Interfaz grafica principal que funciona con widgets
# Siguiendo el tutorial de este video: https://www.youtube.com/watch?v=MpkTYMzhV0A&t=123s

# Importar tkinter:

import tkinter as tk

app = tk.Tk()
palabra = tk.StringVar(app) # Variables para entrada de informacion dentro del widget. Es un objeto
entrada = tk.StringVar(app) # Variables para entrada de informacion dentro del widget. Es un objeto


# Tk() con mayuscula es la ventana principal. Es una clase. Aca estamos creando una instancia de tk

app.geometry("300x600")

# Dimensiones son Anchura x Altura

app.config(background="blue")

# Se configura el color del fondo del widget

tk.Wm.wm_title(app, "Bienvenido")

# Del modulo tk, se llama a la clase de window (Wm) y se le dice que a la ventana de la instancia app se le va a cambiar el nombre

def saludar():
    print("Hola " + entrada.get())

def cambiarLabel():
    palabra.set(entrada.get())

# Funcion que se va a ejecutar cada vez que se le de click al boton definido abajo

tk.Button(
    app,
    text="Click me!",
    font = ("Comic Sans",14),
    bg = "#00a8e8",
    fg="White",
    command=saludar and cambiarLabel, # SIEMPRE USA UNA FUNCION y se pasa como un objeto/variable no como funcion entonces no lleva parentesis    
    # command=lambda: print("Hola qué tal") // Otra opcion podriamos poner lambda: print("") // RECORDATORIO DE QUE LAMBDA se usa para crear funciones anonimas, o sea puede usarse en vez de crear una funcion en el caso de que solamente se use en un solo lugar
        # LAMBDA se usa para funciones de una sola expesion como print("algo")
    relief="flat"
).pack(
    fill=tk.BOTH,
    expand=True
)

# Desde el modulo tk se pueden insertar botones.
# 1. El primero es la app porque es el objeto en donde va a ir
# 2. El texto del boton
# 3. La fuente del boton en una tupla de fuente y tamaño
# 4. bg es el brackground en hexadecimales
# 5. color de la fuente con un fg con color en texto
# 6. command es la fución que va a tener el botón 

# despues de hacer todo se pone un punto y pack para que se empaquete el botón nuevo dentro del módulo app y un "Fill" para que el botón sea igual de grande que el widget => Sin el pack no funciona
# finalmente expand = True para que se expanda si el widget cambia de tamaño

tk.Label(
    app,
    text="Ey soy una etiqueta",
    textvariable=palabra, # mapeo en la label para actualizar el texto de una label
    fg="white",
    bg="black",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True
)


tk.Entry( # AGREGAR TEXTO
    fg="white",
    bg="Red",
    justify="center",
    textvariable=entrada # mapeado de la entrada del widget a la variable entrada de arriba
).pack(
    fill=tk.BOTH,
    expand=True
)

app.mainloop()

# mainloop refresca la app para que se vea en los cambios de manera visual