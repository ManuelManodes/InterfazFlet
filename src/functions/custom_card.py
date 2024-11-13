import flet as ft

class CustomCard(ft.UserControl):
    def __init__(self, image_src, title, subtitle, icon, on_click):
        super().__init__()
        self.image_src = image_src
        self.title = title
        self.subtitle = subtitle
        self.icon = icon
        self.on_click = on_click

    def build(self):
        return ft.Container(
            content=ft.Card(
                elevation=5,
                content=ft.Container(
                    padding=20,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src=self.image_src,
                                width=150,
                                height=150,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            # Los textos han sido eliminados
                            ft.IconButton(
                                icon=self.icon,
                                icon_size=24,
                                tooltip="Más información",
                                on_click=self.on_click,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                ),
            ),
            on_click=self.on_click,
            padding=10,
            border_radius=ft.border_radius.all(10),
        )

    def update_card(self):
        self.update()
