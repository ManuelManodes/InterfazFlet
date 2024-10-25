import flet as ft

def dashboard_page_content():
    return [
        ft.Text("Página de Dashboard", size=24, weight=ft.FontWeight.BOLD, selectable=False),
        ft.Container(
            content=ft.Text("Contenido específico de la página de Dashboard.", selectable=False,),
            bgcolor=ft.colors.TRANSPARENT,
            padding=10,
        ),
        # Agrega más controles relacionados con Layout aquí
    ]
