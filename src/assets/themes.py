# assets/themes.py

import flet as ft

# Paleta de colores para el tema oscuro
DARK_PRIMARY_COLOR = "#17191c"
DARK_SECONDARY_COLOR = "#22252a"
DARK_BACKGROUND_COLOR = "#22252a"
DARK_SELECTION_COLOR = "#FF9F1C"

# Paleta de colores para el tema claro
LIGHT_PRIMARY_COLOR = "#ced4da"
LIGHT_SECONDARY_COLOR = "#ffffff"
LIGHT_BACKGROUND_COLOR = "#ffffff"

def get_dark_theme():
    """
    Retorna un tema oscuro personalizado basado en la paleta de colores proporcionada.
    """
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=DARK_PRIMARY_COLOR,
            on_primary=ft.colors.WHITE,  # Texto e iconos sobre el color primario
            secondary=DARK_SECONDARY_COLOR,
            on_secondary=ft.colors.WHITE,  # Texto e iconos sobre el color secundario
            background=DARK_BACKGROUND_COLOR,
            on_background=ft.colors.WHITE,  # Texto sobre el fondo
            surface=DARK_BACKGROUND_COLOR,
            on_surface=ft.colors.WHITE,  # Texto sobre las superficies
            error=ft.colors.RED_400,
            on_error=ft.colors.WHITE,
            shadow=ft.colors.BLACK54,
        ),
        # Puedes añadir más configuraciones de tema aquí si lo deseas
    )

def get_light_theme():
    """
    Retorna un tema claro personalizado basado en la paleta de colores proporcionada.
    """
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=LIGHT_PRIMARY_COLOR,
            on_primary=ft.colors.BLACK,  # Texto e iconos sobre el color primario
            secondary=LIGHT_SECONDARY_COLOR,
            on_secondary=ft.colors.BLACK,  # Texto e iconos sobre el color secundario
            background=LIGHT_BACKGROUND_COLOR,
            on_background=ft.colors.BLACK,  # Texto sobre el fondo
            surface=LIGHT_BACKGROUND_COLOR,
            on_surface=ft.colors.BLACK,  # Texto sobre las superficies
            error=ft.colors.RED_700,
            on_error=ft.colors.WHITE,
            shadow=ft.colors.BLACK12,
        ),
        # Puedes añadir más configuraciones de tema aquí si lo deseas
    )
