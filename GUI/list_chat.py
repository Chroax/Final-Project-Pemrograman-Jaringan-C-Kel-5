from component import *


def ListChatView(page, cc):
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
                                    Button("Logout", "/sign-in", "Logout", page, cc)
                                ]
                            )
                        ),

                        Container(
                            bgcolor="#292F3F",
                            border_radius=50,
                            height=10000,
                            content=Column(controls=[
                                Divider(height=10, color='transparent'),
                                UserData("Lina Asu Li", "LI", "/msgchat", page, False),
                                Divider(height=10, color="white24"),
                                UserData("Lina Asu Li La Lo Ko Li", "LI", "/msgchat", page, True),
                                Divider(height=10, color="white24")
                            ])
                        )
                    ]),
                )
            ]
        )
    )



