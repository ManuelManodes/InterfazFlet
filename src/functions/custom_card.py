import flet as ft

class CustomCard(ft.UserControl):
    def __init__(self, image_src, on_click):
        super().__init__()
        self.image_src = image_src
        self.on_click = on_click
        self.card = ft.Card(
            elevation=5,
            content=ft.Container(
                padding=10,
                alignment=ft.alignment.center,
                content=ft.Image(
                    src=self.image_src,
                    width=200,
                    height=200,
                    fit=ft.ImageFit.CONTAIN,
                ),
            )
        )
        self.card.content.animate_scale = ft.Animation(
            duration=200, curve=ft.AnimationCurve.EASE_IN_OUT
        )

    def build(self):
        return ft.Container(
            content=self.card,
            on_click=self.on_click,
            on_hover=self.on_hover,
            padding=10,
            border_radius=ft.border_radius.all(10),
        )

    def on_hover(self, e):
        if e.data == 'true':
            self.card.elevation = 8
            self.card.content.scale = ft.transform.Scale(scale=1.03)
        else:
            self.card.elevation = 5
            self.card.content.scale = ft.transform.Scale(scale=1.0)
        self.update()
