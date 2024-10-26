import flet as ft

def client_detail_page_content(page: ft.Page):
    client_name = page.route.split("/")[-1]

    def execute_function_1(e):
        page.snack_bar = ft.SnackBar(content=ft.Text(f"Función 1 ejecutada para {client_name}"))
        page.snack_bar.open()

    def execute_function_2(e):
        page.snack_bar = ft.SnackBar(content=ft.Text(f"Función 2 ejecutada para {client_name}"))
        page.snack_bar.open()

    # Contenido para cada cliente
    return [
        ft.Text(f"Funciones para {client_name}", size=24, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton(text="Función 1", on_click=execute_function_1),
        ft.ElevatedButton(text="Función 2", on_click=execute_function_2),
        ft.ElevatedButton(text="Volver", on_click=lambda e: page.go("/auto_blue_page")),
    ]
