import flet as ft

def main(page: ft.Page):
    page.title = "Utilizando Inputs"

    text_input = ft.TextField(
        label="Nome",
        hint_text="Digite seu nome",
        width=300,
        border_color=ft.Colors.BLUE_300
    ) 

    password_input = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        password=True,
        width=300,
        border_color=ft.Colors.RED_300
    )

    check_box = ft.Checkbox(
        label="Aceitar os termos e condições",
        value=False,
        on_change=lambda e: print(f"Checkbox estado: {e.control.value}")
    )

    cg = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="red", label="Red"),
            ft.Radio(value="green", label="Green"),
            ft.Radio(value="blue", label="Blue"),
        ])
    )

    t = ft.Text()

    def button_clicked(e):
        t.value = f"Sua cor favorita é: {cg.value}"
        page.update()

    color_button = ft.ElevatedButton(
        text="Submit",
        on_click=button_clicked
    )

    dropdown = ft.Dropdown(
        label="Escolha uma opção",
        options=[
            ft.dropdown.Option("Opção 1"),
            ft.dropdown.Option("Opção 2"),
            ft.dropdown.Option("Opção 3"),
            ft.dropdown.Option("Opção 4"),
        ],
        on_change=lambda e: print(f"Opção escolhida: {e.control.value}")
    )

    page.add(
        ft.Column(
            controls = [
                text_input,
                password_input,
                check_box,
                cg,
                t,
                color_button,
                dropdown,
            ]
        )
    )

ft.app(target=main)