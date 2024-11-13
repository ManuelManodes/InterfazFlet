# functions/clientes_blue_page.py

from functions.custom_card import CustomCard
import flet as ft

def clientes_blue_page_content(navigate_to):
    """
    Genera una GridView de CustomCard para la página "Clientes Blue".

    Args:
        navigate_to (function): Función de navegación para cambiar de página.

    Returns:
        ft.GridView: GridView que contiene las instancias de CustomCard.
    """
    tarjetas = [
        CustomCard(
            image_src="assets/images/1-Transbank_CJ_Color_300.png",
            title="Cliente A",
            subtitle="Detalles del Cliente A",
            icon=ft.icons.INFO,
            on_click=lambda e: navigate_to("cliente_a"),
        ),
        CustomCard(
            image_src="assets/images/starkoms_circulo_3_gsuite.png",
            title="Cliente B",
            subtitle="Detalles del Cliente B",
            icon=ft.icons.INFO,
            on_click=lambda e: navigate_to("cliente_b"),
        ),
        # Agrega más CustomCard según sea necesario
    ]

    # Crear una GridView responsiva para organizar las tarjetas
    grid = ft.GridView(
        expand=True,
        runs_count=3,  # Número de columnas
        max_extent=250,  # Máximo ancho de cada tarjeta
        spacing=20,
        run_spacing=20,
        controls=tarjetas,
    )

    return grid
