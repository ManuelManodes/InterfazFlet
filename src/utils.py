# utils.py

import sys
import os

def resource_path(relative_path):
    """
    Obtiene la ruta absoluta del recurso, ya sea en desarrollo o empaquetado.

    Args:
        relative_path (str): Ruta relativa al recurso (por ejemplo, 'images/mi_imagen.png').

    Returns:
        str: Ruta absoluta al recurso.
    """
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Si no está empaquetado, usa la ruta absoluta del directorio actual
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
