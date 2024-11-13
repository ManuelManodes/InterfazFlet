# functions/auto_blue_page.py

from functions.custom_card import CustomCard
import flet as ft

def auto_blue_page_content(navigate_to):
    """
    Genera una GridView de CustomCard para la página "Acceso Rápido".

    Args:
        navigate_to (function): Función de navegación para cambiar de página.

    Returns:
        ft.GridView: GridView que contiene las instancias de CustomCard.
    """
    tarjetas = [
        CustomCard(
            image_src="images/image1.png",  # Ruta relativa a assets_dir
            title="Dashboard",
            subtitle="Visualiza tus métricas clave",
            icon=ft.icons.DASHBOARD,
            on_click=lambda e: navigate_to("dashboard"),
        ),
        CustomCard(
            image_src="images/image2.png",
            title="Clientes",
            subtitle="Gestiona tus clientes Blue",
            icon=ft.icons.PEOPLE,
            on_click=lambda e: navigate_to("clientes_blue"),
        ),
        CustomCard(
            image_src="images/image3.png",
            title="Integraciones",
            subtitle="Conecta con otras aplicaciones",
            icon=ft.icons.INTEGRATION_INSTRUCTIONS,
            on_click=lambda e: navigate_to("integraciones"),
        ),
        CustomCard(
            image_src="images/image4.png",
            title="Reportes",
            subtitle="Genera reportes detallados",
            icon=ft.icons.REPORT,
            on_click=lambda e: navigate_to("reportes"),
        ),
        # Agrega más CustomCard según sea necesario
    ]

    # Crear una GridView responsiva para organizar las tarjetas
    grid = ft.GridView(
        expand=True,
        runs_count=3,      # Número de columnas
        max_extent=250,    # Máximo ancho de cada tarjeta
        spacing=20,
        run_spacing=20,
        controls=tarjetas,
    )

    return grid
