import flet as ft

# Básico 
# def main(page: ft.Page):
#     page.title = "Página exemplo"
#     page.add(
#         ft.ElevatedButton(text="Botão simples"),
#         ft.ElevatedButton("Botão desabilitado", disabled=True)
#     )
#     page.update()

# Com ícones
# def main(page: ft.Page):
#     page.title = "Botão com ícone"
#     page.theme_mode = ft.ThemeMode.LIGHT
#     page.add(
#         ft.ElevatedButton(text="Botão com ícone", icon="access_time"),
#         ft.ElevatedButton(text="Botão desabilitado", icon="park_rounded", icon_color="green400")
#     )
#     page.update()

# Com clique
# def main(page: ft.Page):
#     page.title = "Botão com clique"
# 
#     def button_clicked(e):
#         b.data += 1
#         t.value = f"Botão clicado {b.data} veze(s)"
#         page.update()
# 
#     b = ft.ElevatedButton("Clique", on_click=button_clicked, data=0)
#     t = ft.Text()
# 
#     page.add(b, t)

# Botões elevados com conteúdo customizado
def main(page: ft.Page):
    page.title = "Botão com conteúdo customizado"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        ft.ElevatedButton(
            width=150,
            content=ft.Row([
                ft.Icon(name=ft.Icons.FAVORITE, color="pink"),
                ft.Icon(name=ft.Icons.AUDIO_FILE, color="blue"),
                ft.Icon(name=ft.Icons.BEACH_ACCESS, color="green"),
            ]),
        ),
        ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="Botão composto", size=20),
                        ft.Text(value="Texto secundário", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5
                ),
                padding=ft.padding.all(10)
            )
        )
    )
    page.update()



ft.app(target=main)