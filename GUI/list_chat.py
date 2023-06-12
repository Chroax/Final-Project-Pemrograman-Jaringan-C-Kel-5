from component import *
class Realm():
    def __init__(self, username, realm_id, ip_address, port):
        self.username = username
        self.realm_id = realm_id
        self.ip_address = ip_address
        self.port = port

def ListChatView(page,cc):
    def send_message_click(e, type):
        j = add_realm.value.split(" ")
        realm_id = j[0]
        ip_address = j[1]
        port = j[2]
        if realm_id == "" or ip_address == "" or port == "":
            return
        protocol = "addrealm " + realm_id + " " + ip_address + " " + port
        print(cc.proses(protocol))

    add_realm = TextField(
        hint_text="Add realm ('realmId ipaddress port')",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        color="black",
        bgcolor="white",
        on_submit=lambda e: send_message_click(e, "add"),
        border_radius = 10,
    )

    return Container(
        height=2000,
        bgcolor="#1B202D",  # Set the first background color
        border_radius=10,
        animate=animation.Animation(500, "decelerate"),
        alignment=alignment.top_left,
        content=Column(
            controls=[
                Container(
                    padding=padding.only(top=10),
                    alignment=alignment.center,
                    content=Column(controls=[
                        Container(
                            offset=[0.01, 0, 0, 0],
                            height=70,
                            border_radius=10,
                            alignment=alignment.center,
                            content=Row(
                                controls=[
                                    Text(
                                        value="Message",
                                        weight="bold",
                                        color="white",
                                        size=38,
                                        opacity=1,
                                        animate_opacity=200
                                    ),
                                    Button("Logout", "/sign-in","Logout", page,cc),
                                    add_realm,
                                    IconButton(
                                        icon=icons.ADD_ROUNDED,
                                        tooltip="Add",
                                        on_click=lambda e: send_message_click(e, "add"),
                                        icon_color = "white"
                                    ),
                                ]
                            )
                        ),

                        Container(
                            bgcolor="#292F3F",
                            border_radius=50,
                            height=10000,
                            content=Column(controls=[
                                Divider(height=10, color='transparent'),
                                UserData("Lina Asu Li", "LI", "/msgchat", page, True),
                                Divider(height=10, color="white24"),
                                UserData("Lina Asu Li La Lo Ko Li", "LI", "/anton-kontol", page, True),
                                Divider(height=10, color="white24")
                            ])
                        )
                    ]),
                )
            ]
        )
    )




