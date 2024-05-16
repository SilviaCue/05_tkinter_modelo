
# Importaciones
import os
import tkinter as tk
from tkinter import ttk, filedialog
from diffusers import DiffusionPipeline
from PIL import Image, ImageTk

# Inicializar el modelo
arte = DiffusionPipeline.from_pretrained(
    "lambdalabs/sd-image-variations-diffusers")


# Función para abrir el explorador de archivos y seleccionar varias imagenes
def seleccionar_imagenes():
    rutas_imagenes = filedialog.askopenfilenames()
    if rutas_imagenes:
        imagen_procesada = procesar_imagenes(rutas_imagenes)
        mostrar_imagen_procesada(imagen_procesada)

# Función para procesar una imagen


def procesar_imagenes(rutas_imagenes):
    imagenes_procesadas = []
    for ruta_imagen in rutas_imagenes:
        imagen = Image.open(ruta_imagen)
        imagen_procesada = arte(imagen)
        imagenes_procesadas.append(imagen_procesada)
    imagen_final = sum(imagenes_procesadas) / len(imagenes_procesadas)
    return imagen_final

# Función para mostrar la imagen procesada


def mostrar_imagen_procesada(imagen):
    imagen_final = ImageTk.PhotoImage(imagen)
    panel_imagen.config(image=imagen_final)
    panel_imagen.image = imagen_final


# Crear la ventana principal de Tkinter
ventana = tk.Tk()
ventana.title("Aplicación de Procesamiento de Imágenes")

# Contenedor principal
contenedor = ttk.Frame(ventana, padding=50)
contenedor.grid(row=0, column=0, sticky="nsew", padx=80, pady=80)

# Título con fuente más grande
ttk.Label(contenedor, text="Aplicación de Procesamiento de Imágenes", font=("Arial", 20)).grid(
    row=0, column=0, columnspan=12, pady=(20, 10))

# Objeto de estilo
style = ttk.Style()

# Configuración el estilo del botón
style.configure("Custom.TButton", background="grey",
                foreground="black", font=("Arial", 16), padding=(10, 10))

# Botón para seleccionar imagenes
boton_seleccionar = ttk.Button(
    contenedor, text="Seleccionar Imagen", command=seleccionar_imagenes, style="Custom.TButton")
boton_seleccionar.grid(row=1, column=0, padx=10, pady=20)

# Botón para procesar imagenes
boton_procesar = ttk.Button(contenedor, text="Procesar Imagen", command=lambda: procesar_imagenes(
    mostrar_imagen_procesada), style="Custom.TButton")
boton_procesar.grid(row=1, column=8, padx=10, pady=20)

# Panel para mostrar la imagen procesada
panel_imagen = tk.Label(contenedor)
panel_imagen.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Bucle ejecutar la ventana principal
ventana.mainloop()
