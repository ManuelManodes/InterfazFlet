import flet as ft

def auto_blue_page_content():
    return [
        ft.Text("Acceso automatización Blue", size=24, weight=ft.FontWeight.BOLD, selectable=False),
        ft.Container(
            content=ft.Text("Contenido específico de la página de automatizaciones Blue.", selectable=False),
            bgcolor=ft.colors.TRANSPARENT,
            padding=10,
        ),
        # Agrega más controles relacionados con Navigation aquí
    ]
