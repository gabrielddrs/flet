import flet as ft

def main(page: ft.Page):
    page_title = "Utilizando Alertdialogs e Banner"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    action_button_style = ft.ButtonStyle(color=ft.Colors.BLUE)

    def close_banner(e):
        page.close(banner)
        page.add(ft.Text(f"Clicado: {e.control.text}"))

    banner = ft.Banner(
        bgcolor=ft.Colors.AMBER_100,
        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER,  size=40),
        content=ft.Text(
            value="Erro ao excluir arquivo.",
            color=ft.Colors.BLACK
        ),
        actions=[
            ft.TextButton("Tentar Novamente", action_button_style, on_click=close_banner),
            ft.TextButton("Ignorar", action_button_style, on_click=close_banner),
            ft.TextButton("Cancelar", action_button_style, on_click=close_banner),
        ]
    )

    def show_non_alert(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Olá, isso é um non-model dialog"),
            on_dismiss=lambda e: page.add(ft.Text("Non-Model Dialog dismissed"))
        )
        page.open(dlg)


    def show_modal_dialog(e):
        def handle_close(e):
            page.close(dlg_modal)
            page.add(ft.Text(f"Modal fechado com ação: {e.control.text}"))


        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Por favor, confirme"),
            content=ft.Text("Você realmente deseja apagar todos esses arquivos?"),
            actions=[
                ft.TextButton("Sim", on_click=handle_close),
                ft.TextButton("Não", on_click=handle_close),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: page.add(ft.Text("Modal Dialog Dismised"))
        )

        page.open(dlg_modal)

    page.add(
        ft.Column(
            controls=[
                ft.ElevatedButton("Abrir non-modal dialog", on_click=show_non_alert),
                ft.ElevatedButton("Abrir modal dialog", on_click=show_modal_dialog),
                ft.ElevatedButton("Abrir banner", on_click=lambda e: page.open(banner)),
            ]
        )
    )

ft.app(target=main)