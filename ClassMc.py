import tkinter as tk
from tkinter import ttk, messagebox
import random

class Mc:
    """Clase para mostrar todos los registros en una tabla interactiva."""

    def __init__(self, master, get_record_instance):
        self.__get_record_instance = get_record_instance

        # Cuadro de entrada para buscar registros por ID
        self.search_entry = tk.Entry(master, width=30)
        self.search_entry.pack(pady=10)
        self.search_entry.insert(0, "Buscar por ID")

        # Botón para buscar registros
        tk.Button(master, text="Buscar Registro", command=self.buscar_registro).pack(pady=5)

        # Botón para cargar todos los registros aleatorios
        tk.Button(master, text="Cargar Registros Aleatorios", command=self.cargar_registros_aleatorios).pack(pady=5)

        # Crear el Treeview para mostrar los registros en formato de tabla
        self.tree = ttk.Treeview(master, columns=("ID", "Nombre", "Ciudad", "Circuito"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Ciudad", text="Ciudad")
        self.tree.heading("Circuito", text="Circuito")

        # Ajuste de ancho de las columnas
        self.tree.column("ID", width=30)
        self.tree.column("Nombre", width=100)
        self.tree.column("Ciudad", width=100)
        self.tree.column("Circuito", width=100)

        # Empaquetar el Treeview en la ventana
        self.tree.pack(pady=10)

    def cargar_registros_aleatorios(self):
        """Carga todos los registros desde la API y los muestra en la tabla de manera aleatoria."""
        # Limpiar la tabla antes de cargar nuevos registros
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obtener todos los registros y agregarlos a la tabla
        registros = self.__get_record_instance.get_all_records()

        # Comprobación de registros
        if registros:
            # Barajar los registros
            random.shuffle(registros)
            for registro in registros:
                nombre = registro.get("nombre", "")
                ciudad = registro.get("Ciudad", "")
                circuito = registro.get("circuito", "")

                self.tree.insert("", "end", values=(
                    registro["id"], nombre, ciudad, circuito
                ))
        else:
            messagebox.showinfo("Información", "No se encontraron registros.")

    def buscar_registro(self):
        """Busca y muestra registros que coincidan con el ID ingresado en el cuadro de búsqueda."""
        # Obtener el ID de búsqueda
        search_id = self.search_entry.get().strip()

        # Limpiar la tabla antes de cargar nuevos registros
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obtener todos los registros y agregar los que coinciden a la tabla
        registros = self.__get_record_instance.get_all_records()

        # Comprobación de registros
        if registros:
            for registro in registros:
                # Verificar si el ID coincide con el término de búsqueda
                if search_id == registro["id"]:
                    nombre = registro.get("nombre", "")
                    ciudad = registro.get("Ciudad", "")
                    circuito = registro.get("circuito", "")
                    self.tree.insert("", "end", values=(
                        registro["id"], nombre, ciudad, circuito
                    ))
                    break  # Salir del bucle después de encontrar el registro
            else:
                messagebox.showinfo("Información", "No se encontró el registro con ese ID.")
        else:
            messagebox.showinfo("Información", "No se encontraron registros.")
