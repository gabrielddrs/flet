import flet as ft

def main(page: ft.Page):
    faq_list = [
        {
            "q": "O que é o Flet?",
            "a": "Flet é uma biblioteca Python para criação de interfaces gráficas de formas simples"
        },
        {
            "q": "Como instalar o Flet?",
            "a": "Usando o pip install flet"
        },
        {
            "q": "Onde posso encontrar a documentação?",
            "a": "A documentação está no link: 'http://flet.dev/docs'"
        },
    ]

    def handle_change(e: ft.ControlEvent):
        print(f"Panel: {e.data} toggled")

    def handle_delete(e: ft.ControlEvent):
        panel.controls.remove(e.control.data)
        page.update()

    panel = ft.ExpansionPanelList(
        expand_icon_color=ft.Colors.AMBER,
        elevation=8,
        divider_color=ft.Colors.AMBER,
        on_change=handle_change
    )

    for item in faq_list:
        exp = ft.ExpansionPanel(
            header=ft.ListTile(title=ft.Text(item["q"]))
        )

        exp.content = ft.Column(
            [
                ft.ListTile(
                    title=ft.Text(item["a"])
                ),
                ft.Row(
                    [
                        ft.TextButton("Marcar como útil",
                                      on_click = lambda e, item=item:page.add(
                                          ft.Text(f"Você marcou a resposta: {item['a']} como útil",
                                                  color=ft.Colors.GREEN_600)
                                      )),
                        ft.IconButton(ft.Icons.DELETE,
                                      on_click=handle_delete, data=exp)
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
            ]
        )
        panel.controls.append(exp)

    page.add(panel)

ft.app(target=main)