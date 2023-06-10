import flet as ft

def main(page: ft.Page):
    chat = ft.Column()
    new_message = ft.TextField()
    chat_container=ft.Container(
        width=1280,
        height=720,
        bgcolor="black",
        
    )
    def send_click(e):
        chat.controls.append(ft.Text(new_message.value))
        new_message.value = ""
        page.update()

    page.add(
        chat_container
    )

ft.app(target=main)