import tkinter as tk
from tkinter import messagebox

def add_line_breaks():
    text = input_text.get("1.0", "end") # obtiene el texto del cuadro de entrada
    text = text.replace(".", ".\n") # reemplaza los puntos con puntos seguidos de un salto de línea
    output_text.delete("1.0", "end") # elimina cualquier texto existente en el cuadro de salida
    output_text.insert("1.0", text) # inserta el nuevo texto con los saltos de línea

def copy_to_clipboard():
    text = output_text.get("1.0", "end") # obtiene el texto del cuadro de salida
    root.clipboard_clear() # limpia el portapapeles
    root.clipboard_append(text) # agrega el texto al portapapeles

def remove_line_spaces():
    text = output_text.get("1.0", "end") # obtiene el texto del cuadro de salida
    text = '\n'.join([line.strip() for line in text.splitlines()]) # elimina los espacios al principio y final de cada línea
    output_text.delete("1.0", "end") # elimina cualquier texto existente en el cuadro de salida
    output_text.insert("1.0", text) # inserta el nuevo texto sin espacios al principio y final de cada línea

def clear_text():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")

root = tk.Tk() # crea la ventana principal
root.title("Line Break Adder") # establece el título de la ventana

# crea un cuadro de entrada para el texto
input_text = tk.Text(root, height=10, width=40)
input_text.pack()

# crea un botón para ejecutar la función de agregar saltos de línea
add_breaks_button = tk.Button(root, text="Add Line Breaks", command=add_line_breaks)
add_breaks_button.pack()

# crea un cuadro de salida para mostrar el texto con los saltos de línea agregados
output_text = tk.Text(root, height=10, width=40)
output_text.pack()

# crea un botón para copiar el texto del cuadro de salida al portapapeles
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

# crea un botón para eliminar los espacios al principio y final de cada línea
remove_spaces_button = tk.Button(root, text="Remove Line Spaces", command=remove_line_spaces)
remove_spaces_button.pack()

#crea un botón para limpiar los cuadros de texto
clear_button = tk.Button(root, text="Clear Text", command=clear_text)
clear_button.pack()

root.mainloop() # inicia el bucle de eventos de la GUI

