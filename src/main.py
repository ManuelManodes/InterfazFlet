import flet as ft
from functions.clientes_blue_page import clientes_blue_page_content
from functions.blue.client_detail_page import client_detail_page_content
from assets.themes import get_dark_theme, get_light_theme
from functions.custom_card import CustomCard

def main(page: ft.Page):
    # Configuración inicial
    page.window_width = 800
    page.window_height = 380
    page.window_resizable = True
    page.title = "Interfaz Clientes Blue"
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = get_dark_theme()
    page.padding = 0
    page.spacing = 0
    #page.scroll = ft.ScrollMode.AUTO

    top_bar_height = 60  # Ajustado para una mejor apariencia

    # Función recursiva para actualizar todas las CustomCard
    def update_all_custom_cards(control):
        if isinstance(control, CustomCard):
            control.update_card()
        if hasattr(control, 'controls'):
            for child in control.controls:
                update_all_custom_cards(child)

    # Función para cambiar el tema
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            page.theme = get_dark_theme()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.theme = get_light_theme()

        # Actualizar dinámicamente el color de fondo del sidebar y top_bar
        sidebar.bgcolor = page.theme.color_scheme.secondary
        top_bar.bgcolor = page.theme.color_scheme.secondary

        # Actualizar todas las tarjetas personalizadas
        for control in content_area.controls:
            update_all_custom_cards(control)

        # Actualizar toda la interfaz
        page.update()

    # Función de navegación
    def navigate_to(destination):
        content_area.controls.clear()
        if destination == "clientes_blue":
            content_area.controls.append(clientes_blue_page_content(navigate_to))
        elif destination == "cliente_a":
            content_area.controls.append(client_detail_page_content(page, "Transbank", navigate_to))
        elif destination == "cliente_b":
            content_area.controls.append(client_detail_page_content(page, "Starkoms", navigate_to))
        # Agrega más elif según sea necesario para otros clientes
        page.update()

    # Barra superior
    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.Text(
                    "Interfaz Clientes Blue",
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),
                ft.IconButton(
                    icon=ft.icons.BRIGHTNESS_6,
                    on_click=toggle_theme,
                    tooltip="Cambiar Tema",
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
        ),
        height=top_bar_height,
        bgcolor=page.theme.color_scheme.secondary,
        padding=10,
    )

    # Sidebar con solo la opción "Clientes Blue"
    navigation_rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.APARTMENT_ROUNDED, label="Clientes Blue"
            ),
        ],
        extended=True,
        on_change=lambda e: navigate_to("clientes_blue"),
    )

    # Área de contenido inicial con clientes_blue_page_content
    content_area = ft.Column(
        controls=[clientes_blue_page_content(navigate_to)],
        expand=True,
        spacing=10,
    )

    # Sidebar contenedor
    sidebar = ft.Container(
        content=navigation_rail,
        width=200,
        bgcolor=page.theme.color_scheme.secondary,
        padding=0,
    )

    # Ajustar alturas dinámicamente
    def update_layout_heights():
        available_height = page.window_height - top_bar_height
        sidebar.height = max(available_height, 0)
        content_container.height = max(available_height, 0)
        page.update()

    # Evento al redimensionar ventana
    page.on_resize = lambda e: update_layout_heights()

    # Contenedor para contenido principal
    content_container = ft.Container(
        content=ft.Column([content_area], spacing=10),
        expand=True,
        padding=10,
    )

    # Layout principal
    main_content = ft.Column(
        [
            top_bar,
            ft.Row(
                [
                    sidebar,
                    ft.VerticalDivider(width=1, thickness=1),
                    content_container,
                ],
                spacing=0,
                expand=True,
            ),
        ],
        spacing=0,
    )

    # Agregar contenido principal
    page.add(main_content)
    update_layout_heights()

# Iniciar la aplicación y especificar el directorio de assets
ft.app(target=main, assets_dir="assets")
