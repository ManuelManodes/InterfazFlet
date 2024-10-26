import flet as ft
from functions.auto_blue_page import auto_blue_page_content
from assets.themes import get_dark_theme, get_light_theme

def main(page: ft.Page):
    # Configuración inicial
    page.window.width = 1100
    page.window.height = 600
    page.window.resizable = True

    page.title = "Interfaz automatización Blue"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = get_light_theme()
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO

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

    # Definimos una función de navegación que carga diferentes contenidos
    def navigate_to(destination):
        content_area.controls.clear()
        if destination == "acceso_rapido":
            content_area.controls.extend(auto_blue_page_content(navigate_to))
        elif destination == "dashboard":
            content_area.controls.append(ft.Text("Página del Dashboard"))
        elif destination == "displays":
            content_area.controls.append(ft.Text("Página de Displays"))
        page.update()

    # Barra superior
    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.Text("Interfaz automatización Blue", size=24, weight=ft.FontWeight.BOLD),
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

    # Sidebar con solo la opción de "Acceso rápido"
    navigation_rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME, label="Acceso rápido"
            ),
        ],
        extended=True,
        on_change=lambda e: navigate_to("acceso_rapido"),
    )

    # Área de contenido inicial con auto_blue_page_content
    content_area = ft.Column(
        controls=auto_blue_page_content(navigate_to),  # Mostrar contenido inicial
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
        available_height = page.height - top_bar_height
        sidebar.height = max(available_height, 0)
        content_container.height = max(available_height, 0)
        page.update()

    # Evento al redimensionar ventana
    page.on_resized = lambda e: update_layout_heights()

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

# Iniciar la aplicación
ft.app(target=main)
