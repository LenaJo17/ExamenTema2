import tkinter as tk
from ClassMc import Mc
from ClassRecord import classRecord

class AppDB:
    def __init__(self):
        self.root = tk.Tk()  # Crear la ventana principal
        self.root.title("Registro Motocross")
        self.root.geometry("500x400")
        self.root.resizable(False, False)  # La ventana no es dimensionable

        self.get_record_instance = classRecord()  # Instancia de classRecord
        self.show_record_instance = Mc(self.root, self.get_record_instance)  # Instancia de Mc

        self.root.mainloop()  # Iniciar la aplicación

# Ejecución de la aplicación
if __name__ == "__main__":
    AppDB()  # Instancia y ejecuta la aplicación




