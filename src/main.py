import flet as ft
from functions.dashboard_page import dashboard_page_content
from functions.auto_blue_page import auto_blue_page_content
from assets.themes import get_dark_theme, get_light_theme

def main(page: ft.Page):
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = True

    page.title = "Interfaz automatización Blue"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = get_light_theme()
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO

    top_bar_height = 50
    top_bar = ft.Container(
        height=top_bar_height,
        bgcolor=page.theme.color_scheme.secondary,
        alignment=ft.alignment.center_left,
        padding=ft.padding.only(left=10),
    )

    def toggle_theme():
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            page.theme = get_dark_theme()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.theme = get_light_theme()

        top_bar.bgcolor = page.theme.color_scheme.secondary
        sidebar.bgcolor = page.theme.color_scheme.secondary
        page.update()

    # Variable para almacenar el índice anterior
    previous_selected_index = [0]  # Usamos una lista para que sea mutable dentro de los closures

    def change_page(e):
        selected = e.control.selected_index
        num_pages = len(navigation_rail.destinations) - 1

        if selected < num_pages:
            if selected == 0:
                content_area.controls = dashboard_page_content()
            elif selected == 1:
                content_area.controls = auto_blue_page_content()
            content_area.update()
        else:
            toggle_theme()
            # Restablecer al índice anterior
            navigation_rail.selected_index = previous_selected_index[0]
            navigation_rail.update()

        # Guardar el índice actual como el anterior para la próxima vez
        previous_selected_index[0] = selected

    navigation_rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.GRID_VIEW, label="Dashboard"),
            ft.NavigationRailDestination(icon=ft.icons.ARROW_FORWARD, label="Acceso a Blue"),
            ft.NavigationRailDestination(icon=ft.icons.BRIGHTNESS_6, label="Cambiar Tema"),
        ],
        extended=True,
        on_change=change_page,
    )

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

    def update_layout_heights():
        available_height = page.height - top_bar.height
        sidebar.height = max(available_height, 0)
        content_container.height = max(available_height, 0)
        page.update()

    page.on_resized = lambda e: update_layout_heights()

    content_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Interfaz automatización Blue", size=24, weight=ft.FontWeight.BOLD, selectable=False),
                content_area,
            ],
            spacing=10,
        ),
        expand=True,
        padding=10,
    )

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
