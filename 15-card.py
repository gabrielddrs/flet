import flet as ft

def main(page: ft.Page):
    page.title = "Cartão de Aniversário"

    card_content = ft.Column(
        [
            ft.ListTile(
                leading=ft.Icon(ft.Icons.CAKE),
                title=ft.Text("Feliz Aniversário!", size=25, weight="bold"),
                subtitle=ft.Text("Seu dia seja repleto de alegrias, risadas e muito amor.")
            ),
            ft.Row(
                [
                    ft.TextButton("Compartilhar",
                                  on_click=lambda e: page.add(ft.Text("Mensagem compartilhada com sucesso",
                                                                      color=ft.Colors.GREEN_600))),
                    ft.TextButton("Enviar Votos")
                ],
                alignment=ft.MainAxisAlignment.END
            )
        ]
    )

    page.add(
        ft.Card(
            content=ft.Container(
                content=card_content,
                width=400,
                padding=20
            )
        )
    )

ft.app(target=main)