import requests
from tkinter import messagebox


class classRecord:
    """Clase para manejar las solicitudes a la API."""

    def __init__(self):
        self.__url = "https://671be4342c842d92c381a5e8.mockapi.io/Motocross"

    def get_all_records(self):
        """Obtiene todos los registros desde la API."""
        try:
            respuesta = requests.get(self.__url)
            respuesta.raise_for_status()
            datos = respuesta.json()

            # Mensaje de depuración para verificar la estructura de datos
            print("Estructura de datos recibidos:", datos)

            return datos if datos else []
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo obtener los registros: {e}")
            return []
