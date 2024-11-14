import flet as ft

def client_detail_page_content(page: ft.Page, client_name, navigate_to):
    # Definir las funciones para cada botón
    def execute_function_1(e):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Función 1 ejecutada para {client_name}", color=page.theme.color_scheme.on_surface),
            bgcolor=page.theme.color_scheme.surface
        )
        page.snack_bar.open()

    def execute_function_2(e):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Función 2 ejecutada para {client_name}", color=page.theme.color_scheme.on_surface),
            bgcolor=page.theme.color_scheme.surface
        )
        page.snack_bar.open()

    def execute_function_a(e):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Función A ejecutada para {client_name}", color=page.theme.color_scheme.on_surface),
            bgcolor=page.theme.color_scheme.surface
        )
        page.snack_bar.open()

    # Obtener colores del tema actual
    text_color = page.theme.color_scheme.on_background
    button_bgcolor = page.theme.color_scheme.primary
    button_text_color = page.theme.color_scheme.on_primary

    # Mapeo de clientes a sus funciones y botones
    client_functions = {
        'transbank': [
            {'text': 'Función 1', 'on_click': execute_function_1},
            {'text': 'Función 2', 'on_click': execute_function_2},
        ],
        'starkoms': [
            {'text': 'Función A', 'on_click': execute_function_a},
        ],
        # Puedes agregar más clientes y sus funciones aquí
    }

    # Contenido para cada cliente
    controls = [
        ft.Text(
            f"¿Qué quieres procesar en {client_name}?",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=text_color
        )
    ]

    # Obtener las funciones para el cliente actual
    client_funcs = client_functions.get(client_name.lower())

    if client_funcs:
        for func in client_funcs:
            controls.append(
                ft.ElevatedButton(
                    text=func['text'],
                    on_click=func['on_click'],
                    bgcolor=button_bgcolor,
                    color=button_text_color
                )
            )
    else:
        controls.append(
            ft.Text("No hay funciones disponibles para este cliente.", color=text_color)
        )

    # Botón "Volver" con colores fijos
    controls.append(
    ft.ElevatedButton(
        text="Volver",
        on_click=lambda e: navigate_to("clientes_blue"),
        bgcolor=ft.colors.ORANGE_200,  # Color de fondo fijo
        color=ft.colors.ORANGE_ACCENT_700    # Color de texto fijo
    )
)


    return ft.Column(
        controls=controls,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )
