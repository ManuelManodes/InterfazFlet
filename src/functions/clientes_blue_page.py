from functions.custom_card import CustomCard
import flet as ft

def clientes_blue_page_content(navigate_to):
    def create_card(client_name, image_src):
        return CustomCard(
            image_src=image_src,
            on_click=lambda e, dest=client_name: navigate_to(dest),
        )

    tarjetas = [
        create_card("cliente_a", "images/1-Transbank_CJ_Color_300.png"),
        create_card("cliente_b", "images/starkoms_circulo_3_gsuite.png"),
        # Agrega más tarjetas según sea necesario
    ]

    grid = ft.GridView(
        controls=tarjetas,
        max_extent=250,
        child_aspect_ratio=1,
        spacing=20,
        run_spacing=20,
    )

    return ft.Container(
        content=grid,
        alignment=ft.alignment.center,
        expand=True,
    )
