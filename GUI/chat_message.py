import flet as ft

class Message():
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type

class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment="center"
        self.controls=[
                ft.CircleAvatar(
                    content=ft.Text(self.get_initials(message.user_name)),
                    color=ft.colors.WHITE,
                    bgcolor=self.get_avatar_color(message.user_name),
                ),
                ft.Column(
                    [
                        ft.Text(message.user_name, weight="bold", color="white"),
                        ft.Container(
                            bgcolor="#7A8194", 
                            padding=8, 
                            content= ft.Text(message.text, selectable=True, color="white"),
                            border_radius=4,
                            )
                    ],
                    tight=True,
                   
                    spacing=5,
                ),
            ]

    def get_initials(self, user_name: str):
        return user_name[:1].capitalize()

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


def ChatMessageView(page):
    def send_message_click(e):
        user_name = "Afdal"
        if new_message.value != "":
            page.pubsub.send_all(Message(user_name,new_message.value, message_type="chat_message"))
            new_message.value = ""
            new_message.focus()
            page.update()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        color="white",
        bgcolor="#7A8194",
        on_submit=send_message_click,
    )
    submit_row = ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.ATTACH_FILE_ROUNDED,
                    tooltip="Send File",
                    on_click=send_message_click,
                ),
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                ),
            ]
        )
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )
    chatBox = ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
            bgcolor="#3D4354"
        )
    
    msg_container = ft.Container(
        content= submit_row,
        border=ft.border.all(1, ft.colors.OUTLINE),
        border_radius=5,
        # width=1600,
        # height=900,
        padding=10,
        # expand=True,
        bgcolor="#ffffff"
    )
    msg_column = ft.Column(
        controls=[chatBox,msg_container],
        height=720,
        alignment=ft.MainAxisAlignment.START,
    )
    return ft.Container(
        content=msg_column
    )
            
                
        
       
    
        
    