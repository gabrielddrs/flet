import flet as ft

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    # Adicionando uma imagem
    img = ft.Image(
        src='https://pbs.twimg.com/media/EkYuOPUWkAI-fee.jpg:large',
        border_radius=ft.border_radius.all(40),
        height=1000,
        width=1000,
        tooltip="Zé Oreia"
    )

    page.add(img)
    page.update()

ft.app(target=main)