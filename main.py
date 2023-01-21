import tkinter as tk
from tkinter import messagebox

def add_line_breaks():
    text = input_text.get("1.0", "end") # obtiene el texto del cuadro de entrada
    output_text.delete("1.0", "end") # elimina cualquier texto existente en el cuadro de salida
    output_text.insert("1.0", text) # inserta el nuevo texto con los saltos de línea

def copy_to_clipboard():
    root.clipboard_clear() # limpia el portapapeles
    root.clipboard_append(text) # agrega el texto al portapapeles

def remove_line_spaces():
    output_text.delete("1.0", "end") # elimina cualquier texto existente en el cuadro de salida
    output_text.insert("1.0", text) # inserta el nuevo texto sin espacios al principio y final de cada línea

def clear_text():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")

root = tk.Tk()
root.title("Line Break Adder")

input_text = tk.Text(root, height=10, width=40)
input_text.pack()

add_breaks_button = tk.Button(root, text="Add Line Breaks", command=add_line_breaks)
add_breaks_button.pack()

output_text = tk.Text(root, height=10, width=40)
output_text.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

remove_spaces_button = tk.Button(root, text="Remove Line Spaces", command=remove_line_spaces)
remove_spaces_button.pack()

clear_button = tk.Button(root, text="Clear Text", command=clear_text)
clear_button.pack()

root.mainloop()



