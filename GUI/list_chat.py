from component import *
class Realm():
    def __init__(self,realm_id, ip_address, port):
        self.realm_id = realm_id
        self.ip_address = ip_address
        self.port = port


def ListChatView(page,cc):
    realmid_list=[]
    def send_message_click(e, type):
        if(type == "refresh"):
            realm_list = cc.proses("connectedrealm ")
            for realm_id in realm_list:
                realm_columm.controls.append(UserData(realm_id, ip_address, "/msgchat/"+realm_id, page, False))
                realm_columm.controls.append(Divider(height=10, color="white24"))
        else:
            page.update()
            j = add_realm.value.split(" ")
            realm_id = j[0]
            ip_address = j[1]
            port = j[2]
            if realm_id == "" or ip_address == "" or port == "":
                return
            protocol = "addrealm " + realm_id + " " + ip_address + " " + port
            # temp_realm = Realm(realm_id, ip_address, port)
            # realm_list.append(temp_realm)
        
            print(cc.proses(protocol))
            realm_list = cc.proses("connectedrealm ")
            for realm_id in realm_list:
                realm_columm.controls.append(UserData(realm_id, ip_address, "/msgchat/"+realm_id, page, False))
                realm_columm.controls.append(Divider(height=10, color="white24"))
            
            page.update()
        

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
    

    realm_columm = Column(
        controls=[
            Divider(height=10, color="white24"), 
            # UserData("afdal", "afdal", "/msgchat/afdal", page, False),
            # Divider(height=10, color="white24"),
            # UserData("anton", "anton", "/msgchat/anton", page, False),
            # Divider(height=10, color="white24"),
            # UserData("frederick", "frederick", "/msgchat/frederick", page, False),
            # Divider(height=10, color="white24"),
            # UserData("ariq", "ariq", "/msgchat/ariq", page, False),
            # Divider(height=10, color="white24"),
            # UserData("marcel", "marcel", "/msgchat/marcel", page, False),
            # Divider(height=10, color="white24"),
            # UserData("cahyadi", "cahyadi", "/msgchat/cahyadi", page, False),
            # Divider(height=10, color="white24"),
            ] 
    )
    # for realm_id in realm_list:
    #     print(realm_id)
    #     realm_columm.controls.append(Divider(height=10, color="white24"))
    #     realm_columm.controls.append(UserData(realm_id, realm_id, "/msgchat/"+realm_id, page, False))

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
                                    IconButton(
                                        icon=icons.REFRESH_ROUNDED,
                                        tooltip="Refresh",
                                        on_click=lambda e : send_message_click("refresh"),
                                        icon_color = "white",
                                    ),
                                ]
                            )
                        ),

                        Container(
                            bgcolor="#292F3F",
                            border_radius=50,
                            height=10000,
                            content=realm_columm,
                        )
                    ]),
                )
            ]
        )
    )




