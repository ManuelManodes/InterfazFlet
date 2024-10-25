import flet as ft

# Paleta de colores para el tema oscuro
DARK_PRIMARY_COLOR = "#17191c"
DARK_SECONDARY_COLOR = "#22252a"
DARK_BACKGROUND_COLOR = "#22252a"
DARK_SELECTION_COLOR="#FF9F1C"

# Paleta de colores para el tema claro
LIGHT_PRIMARY_COLOR = "#ced4da"
LIGHT_SECONDARY_COLOR = "#ffffff"
LIGHT_BACKGROUND_COLOR = "#ffffff"

def get_dark_theme():
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=DARK_PRIMARY_COLOR,
            secondary=DARK_SECONDARY_COLOR,
            background=DARK_BACKGROUND_COLOR,
            surface=DARK_BACKGROUND_COLOR,
            on_primary=ft.colors.WHITE,
            on_secondary=ft.colors.WHITE,
            on_background=ft.colors.WHITE,
            on_surface=ft.colors.WHITE,
        )
    )

def get_light_theme():
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=LIGHT_PRIMARY_COLOR,
            secondary=LIGHT_SECONDARY_COLOR,
            background=LIGHT_BACKGROUND_COLOR,
            surface=LIGHT_BACKGROUND_COLOR,
            on_primary=ft.colors.BLACK,
            on_secondary=ft.colors.BLACK,
            on_background=ft.colors.BLACK,
            on_surface=ft.colors.BLACK,
        )
    )
