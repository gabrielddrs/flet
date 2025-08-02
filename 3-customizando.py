import flet as ft

def main(page: ft.Page):
    page.title = "Flet do GD"
    # page.bgcolor = "#red"
    # page.bgcolor = "#C79030"
    # page.bgcolor = ft.colors.black

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.padding = ft.padding.all(100)

    page.add(
        ft.Text(value="Hello World"),
        ft.Container(ft.Text(value="Hello World"), bgcolor=ft.Colors.WHITE)
    )

    # Configurando o Desktop
    page.window_height = 300
    page.window_width = 600
    page.window.resizable = False

    # Posicionamento da janela
    page.window_top = 300
    page.window_left = 300

    page.window_progress_bar = 1

    page.update()

ft.app(target=main)