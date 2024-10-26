import flet as ft

def auto_blue_page_content(navigate_to):
    return [
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Bienvenido a la automatización Blue",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLUE_GREY_900,
                    ),
                    ft.Text(
                        "Elige una opción para continuar:",
                        size=16,
                        color=ft.colors.BLUE_GREY_600,
                    ),
                    ft.Row(
                        [
                            # Tarjeta 1: Dashboard
                            ft.Container(
                                content=ft.Card(
                                    content=ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Icon(
                                                    ft.icons.DASHBOARD,
                                                    size=30,
                                                    color=ft.colors.BLUE,
                                                ),
                                                ft.Text(
                                                    "Dashboard",
                                                    size=18,
                                                    weight=ft.FontWeight.BOLD,
                                                    text_align=ft.TextAlign.CENTER,
                                                ),
                                                ft.Text(
                                                    "Ver estadísticas principales.",
                                                    size=12,
                                                    text_align=ft.TextAlign.CENTER,  # Centrar el subtítulo
                                                ),
                                            ],
                                            spacing=4,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        padding=15,  # Reducción del padding interno
                                    ),
                                    elevation=8,  # Menor elevación para estilo compacto
                                    width=240,  # Ancho fijo de la tarjeta
                                    height=120,  # Altura fija de la tarjeta
                                ),
                                on_click=lambda e: navigate_to(0),  # Ir al Dashboard
                                padding=5,
                                ink=True,
                            ),

                            # Tarjeta 2: Displays
                            ft.Container(
                                content=ft.Card(
                                    content=ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Icon(
                                                    ft.icons.VIDEO_LABEL,
                                                    size=30,
                                                    color=ft.colors.GREEN,
                                                ),
                                                ft.Text(
                                                    "Displays",
                                                    size=18,
                                                    weight=ft.FontWeight.BOLD,
                                                    text_align=ft.TextAlign.CENTER,
                                                ),
                                                ft.Text(
                                                    "Gestiona los displays disponibles.",
                                                    size=12,
                                                    text_align=ft.TextAlign.CENTER,  # Centrar el subtítulo
                                                ),
                                            ],
                                            spacing=4,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        padding=15,
                                    ),
                                    elevation=8,
                                    width=240,
                                    height=120,
                                ),
                                on_click=lambda e: navigate_to(1),  # Ir a Displays
                                padding=5,
                                ink=True,
                            ),

                            # Tarjeta 3: Nueva Página
                            ft.Container(
                                content=ft.Card(
                                    content=ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Icon(
                                                    ft.icons.NOTE,
                                                    size=30,
                                                    color=ft.colors.ORANGE,
                                                ),
                                                ft.Text(
                                                    "Nueva Página",
                                                    size=18,
                                                    weight=ft.FontWeight.BOLD,
                                                    text_align=ft.TextAlign.CENTER,
                                                ),
                                                ft.Text(
                                                    "Accede a la nueva página.",
                                                    size=12,
                                                    text_align=ft.TextAlign.CENTER,  # Centrar el subtítulo
                                                ),
                                            ],
                                            spacing=4,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        padding=15,
                                    ),
                                    elevation=8,
                                    width=240,
                                    height=120,
                                ),
                                on_click=lambda e: navigate_to(2),  # Ir a Nueva Página
                                padding=5,
                                ink=True,
                            ),
                        ],
                        spacing=10,  # Menor espacio entre tarjetas
                        alignment=ft.MainAxisAlignment.CENTER,  # Centrar horizontalmente
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,  # Espacio entre el título y las tarjetas
            ),
            expand=True,  # Asegurar que ocupe toda la pantalla
            padding=20,  # Espacio alrededor del contenido
        )
    ]
