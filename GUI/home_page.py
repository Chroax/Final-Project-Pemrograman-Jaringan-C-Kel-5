import flet as ft

def main(page: ft.Page):
    
    # Add everything to the page
    page.add(
        ft.Container(
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Row([
                            ft.Container(
                                content=ft.Text("Private", color="white"),
                                bgcolor="#7A8194",
                                padding=16,
                                border_radius=8,
                            ),
                            ft.Container(
                                content=ft.Text("Group", color="white"),
                                bgcolor="#7A8194",
                                padding=16,
                                border_radius=8,
                            ),
                        ])
                    ),
                    
                    ft.Container(
                        content=ft.Text("Logout", color="white"),
                        bgcolor="#3F65BC",
                        padding=16,
                        border_radius=8,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=60,
            expand=True,
            bgcolor="#3D4354",
        ),
    )

ft.app(port=8550, target=main, view=ft.WEB_BROWSER)