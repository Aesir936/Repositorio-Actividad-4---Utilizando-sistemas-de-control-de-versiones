import tkinter as tk
from tkinter import messagebox

def on_click(event):
    current = entry.get()
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Operación inválida")
            entry.delete(0, tk.END)
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear una entrada para mostrar los números y resultados
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Lista de botones
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Crear y colocar los botones en la ventana
row_value = 1
col_value = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 20), padx=20, pady=20)
    button.grid(row=row_value, column=col_value)
    button.bind("<Button-1>", on_click)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Ejecutar la aplicación
root.mainloop()
