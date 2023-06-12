import flet
from flet import *
import time
from math import pi

class ModernNavBar(UserControl):
    def __init__(self):
        super().__init__()

    def UserData(self,  name : str,):
        #first row has user info, different from the icon rows, so we create a separate function for it
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor=self.get_avatar_color(name),
                        alignment=alignment.center,
                        border_radius=42,
                        content=Text(
                            value=self.get_initials(name),
                            size=20,
                            weight="bold",
                            color="white",
                        ),
                    ),
                    Column(
                        offset=[0, 0, 0, 0.6],
                        spacing=1,
                        alignment="center",
                        controls=[
                            Text(
                                value=name,
                                size=21,
                                weight="bold",
                                color="white",
                                opacity=1,
                                animate_opacity=200
                            ),

                        ]
                 )
            ]
        )
    )

    def TopMessages(self, text: str):
        return Container(
            offset=[0, 0, 0, 10],
            width=200,
            height=70,
            border_radius=10,
            alignment=alignment.center,
            content=Row(
                controls=[

                Text(
                    value=text,
                    weight="bold",
                    color="white",
                    size=38,
                    opacity=1,
                    animate_opacity=200,

                )

            ]
        )
    )
    def get_initials(self, user_name: str):
        return user_name[:1].capitalize()
    
    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            "#FFC107",  # AMBER
            "#2196F3",  # BLUE
            "#795548",  # BROWN
            "#00BCD4",  # CYAN
            "#4CAF50",  # GREEN
            "#3F51B5",  # INDIGO
            "#CDDC39",  # LIME
            "#FF9800",  # ORANGE
            "#E91E63",  # PINK
            "#9C27B0",  # PURPLE
            "#F44336",  # RED
            "#009688",  # TEAL
            "#FFEB3B",  # YELLOW
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]

    def build(self):
        return Container(width=500,
                         height=580,padding=padding.only(top=10, left=10, right=10),
                         alignment=alignment.center,
                         content=Column(controls=[
                             #
                             self.TopMessages( "Messages"),
                             self.UserData("Antonio",),
                             Divider(height=10, color="white24"),
                             self.UserData("Afdal",),
                             Divider(height=10, color="white24"),
                             self.UserData("Cahyadi",),
                             Divider(height=10, color="white24"),
                             self.UserData("Frederick",),
                             Divider(height=10, color="white24"),
                             self.UserData("Ariq", ),
                         ]

                         ),
                         )

def main(page : Page):
    #title
    page.title= 'Flet Modern Sidebar'
    #dimensions
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#1f262f"

    #main page controls
    page.add(
        Container(width=480,
                  height=590,
                  bgcolor="black",  # Set the first background color
                  border_radius=10,
                  animate=animation.Animation(500, "decelerate"),
                  alignment=alignment.center,
                  content=Column(
                      controls=[
                      Container(
                          width="100%",
                          height="50%",
                          bgcolor="black",  # Set the second background color
                          content= ModernNavBar()
                      ),

                  ])
        )
    )

    page.update()


if __name__ == "__main__":
    flet.app(target=main)