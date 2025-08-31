import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_dismissal(e): 
        page.add(ft.Text("drawer dismissed"))

    def handle_change(e): 
        page.add(ft.Text(f"Selected Index Changed: {e.selected_index}"))

    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label = "Item 1",
                icon = ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon = ft.Icon(ft.Icons.DOOR_BACK_DOOR)
            ),
            ft.Divider(thickness=2),
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label = "Item 2",
                icon = ft.Icons.MAIL_OUTLINED,
                selected_icon = ft.Icons.MAIL
            ),
            ft.NavigationDrawerDestination(
                label = "Item 3",
                icon = ft.Icons.PHONE_OUTLINED,
                selected_icon = ft.Icons.PHONE
            ),
        ]
    )

    page.add(ft.ElevatedButton("Show Drawer", on_click=lambda e: page.open(drawer)))

ft.app(target=main)