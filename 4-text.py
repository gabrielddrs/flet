import flet as ft

def main(page: ft.Page):
    t1 = ft.Text(
        value="Utilizando elemento de texto",
        theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.Colors.WHITE30,
        style=ft.TextStyle(
            color=ft.Colors.BLACK38,
            font_family="Arial",
            weight=ft.FontWeight.W_300,
            italic=True
        ),
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS,
        text_align=ft.TextAlign.CENTER
    )

    t2 = ft.Text(
        spans=[
            ft.TextSpan(text="Texto de exemplo", url="https://www.google.com")
        ]
    )

    # Adiciona os textos dentro de uma linha centralizada
    page.add(
        ft.Row([t1], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([t2], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
