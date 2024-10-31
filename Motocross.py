import tkinter as tk
from tkinter import messagebox
import requests

# Función para obtener todos los registros desde la API
def obtener_registros():
    try:
        url = "https://671be4342c842d92c381a5e8.mockapi.io/Motocross"
        response = requests.get(url)
        response.raise_for_status()  # Verifica si hubo un error en la solicitud
        data = response.json()

        # Verifica si hay registros
        if data:
            mostrar_tabla(data)
        else:
            messagebox.showinfo("Información", "No se encontraron registros.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

# Función para mostrar los registros en una tabla (Listbox)
def mostrar_tabla(registros):
    listbox.delete(0, tk.END)  # Limpia la lista

    # Agrega cada registro en la lista
    for registro in registros:
        listbox.insert(tk.END, f"ID: {registro['id']} - {registro['nombre']} {registro['apellido']}")

    # Almacena los registros para mostrarlos cuando se seleccionen
    global todos_registros
    todos_registros = registros

# Función para mostrar los datos detallados del registro seleccionado
def mostrar_datos(event):
    seleccion = listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        registro = todos_registros[indice]
        texto = (
            f"ID: {registro['id']}\n"
            f"Nombre: {registro['nombre']}\n"
            f"Apellido: {registro['apellido']}\n"
            f"Ciudad: {registro['ciudad']}\n"
            f"Circuito: {registro['calle']}"
        )
        resultado_label.config(text=texto)

# Configuración de la interfaz gráfica
app = tk.Tk()
app.title("Registro Estudiante")
app.geometry("500x300")

# Botón para obtener todos los registros
boton = tk.Button(app, text="Obtener Registros", command=obtener_registros)
boton.pack(pady=10)

# Listbox para mostrar todos los registros
listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", mostrar_datos)

# Label para mostrar los resultados detallados
resultado_label = tk.Label(app, text="", justify="left", font=("Arial", 12))
resultado_label.pack(pady=10)

# Iniciar la aplicación
app.mainloop()