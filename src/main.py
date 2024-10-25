import flet as ft
from functions.dashboard_page import dashboard_page_content
from functions.auto_blue_page import auto_blue_page_content
from assets.themes import get_dark_theme, get_light_theme

def main(page: ft.Page):
    # Establecer dimensiones iniciales
    page.window.width = 800
    page.window.height = 500
    page.window.resizable = True

    page.title = "Interfaz automatización Blue"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = get_light_theme()
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO

    # Definir la altura de la barra superior
    top_bar_height = 50

    # Función para cambiar el tema
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            page.theme = get_dark_theme()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.theme = get_light_theme()

        top_bar.bgcolor = page.theme.color_scheme.secondary
        sidebar.bgcolor = page.theme.color_scheme.secondary
        page.update()

    # Barra superior con el botón para cambiar de tema alineado a la derecha
    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.Text("Interfaz automatización Blue", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(
                    icon=ft.icons.BRIGHTNESS_6,  # Icono del tema
                    on_click=toggle_theme,
                    tooltip="Cambiar Tema",
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Alinear contenido en extremos opuestos
            expand=True,
        ),
        height=top_bar_height,
        bgcolor=page.theme.color_scheme.secondary,
        padding=ft.padding.symmetric(horizontal=10),  # Espacio horizontal en la barra
    )

    # Variable para almacenar el índice anterior
    previous_selected_index = [0]

    # Función para cambiar de página
    def change_page(e):
        selected = e.control.selected_index
        num_pages = len(navigation_rail.destinations)

        if selected < num_pages:
            if selected == 0:
                content_area.controls = dashboard_page_content()
            elif selected == 1:
                content_area.controls = auto_blue_page_content()
            content_area.update()

        # Guardar el índice actual como el anterior para la próxima vez
        previous_selected_index[0] = selected

    # Sidebar de navegación
    navigation_rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.GRID_VIEW, label="Dashboard"),
            ft.NavigationRailDestination(icon=ft.icons.ARROW_FORWARD, label="Acceso a Blue"),
        ],
        extended=True,
        on_change=change_page,
    )

    # Área de contenido que se actualizará
    content_area = ft.Column(
        controls=dashboard_page_content(),
        expand=True,
        spacing=10,
    )

    sidebar = ft.Container(
        content=navigation_rail,
        width=200,
        bgcolor=page.theme.color_scheme.secondary,
        padding=0,
    )

    # Función para actualizar las alturas del sidebar y el área de contenido
    def update_layout_heights():
        available_height = page.height - top_bar_height
        sidebar.height = max(available_height, 0)
        content_container.height = max(available_height, 0)
        page.update()

    page.on_resized = lambda e: update_layout_heights()

    content_container = ft.Container(
        content=ft.Column(
            [content_area],
            spacing=10,
        ),
        expand=True,
        padding=10,
    )

    # Layout principal con la barra superior y la navegación lateral
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

    page.add(main_content)
    update_layout_heights()

ft.app(target=main)
