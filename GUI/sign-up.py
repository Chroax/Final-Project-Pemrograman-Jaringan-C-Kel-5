import flet
from flet import *

import time
from math import pi


class SignInButton(UserControl):
    def __init__(self, btn_name):
        self.btn_name = btn_name
        super().__init__()

    def build(self):
        return Container(
            content=ElevatedButton(
                content=Text(
                    self.btn_name,
                    size=16,
                    weight="bold",
                    font_family="Consolas"
                ),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=8)
                    },
                    color={
                        "": "black"
                    },
                    bgcolor={
                        "": "#7df6dd"
                    }
                ),
                height=42,
                width=320
            )
        )

class AnimationBox(UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        super().__init__()

    def build(self):
        # Rotation Boxes
        return Container(
            width=48,
            height=48,
            border=border.all(2.5, self.border_color),
            bgcolor=self.bg_color,
            border_radius=2,
            rotate=transform.Rotate(
                self.rotate_angle,
                alignment.center
            ),
            animate_rotation=animation.Animation(700, "easeInOut")
        )

class InputField(UserControl):
    def __init__(self, bg_color, icon_name, text_hint, hide, function_emails):
        self.icon_name = icon_name
        self.bg_color = bg_color
        self.text_hint = text_hint
        self.hide = hide
        self.function_emails = function_emails
        super().__init__()

    def return_email_prefix(self, e):
        email = self.controls[0].content.controls[1].value
        if e.control.data in email:
            pass
        else:
            self.controls[0].content.controls[1].value += e.control.data
            self.controls[0].content.controls[2].offset = transform.Offset(0.5, 0)
            self.controls[0].content.controls[2].opacity = 0
            self.update()

    def prefix_email_containers(self):
        email_labels = ["@kelompok5.com", "@kelompok6.com", "@kelompok7.com"]
        label_title = ["KEL5", "KEL6", "KEL7"]
        __ = Row(
            spacing=1,
            alignment=MainAxisAlignment.END
        )
        for index, label in enumerate(email_labels):
            __.controls.append(
                Container(
                    width=45,
                    height=30,
                    alignment=alignment.center,
                    data=label,
                    on_click= lambda e: self.return_email_prefix(e),
                    content=Text(
                        label_title[index],
                        size=9,
                        weight="bold",
                        font_family="Consolas"
                    )
                )
            )
        return Row(
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.END,
            spacing=2,
            opacity=0,
            animate_opacity=200,
            offset=transform.Offset(0.35, 0),
            animate_offset=animation.Animation(400, 'decelerate'),
            controls=[__]
        )

    def get_prefix_email(self, e):
        if self.function_emails:
            email = self.controls[0].content.controls[1].value
            if e.data:
                if "@kelompok5.com" in email or "@kelompok6.com" in email or "@kelompok7.com" in email or "@" in email:
                    self.controls[0].content.controls[2].offset = transform.Offset(0, 0)
                    self.controls[0].content.controls[2].opacity = 0
                    self.update()
                else:
                    self.controls[0].content.controls[2].offset = transform.Offset(-0.9, 0)
                    self.controls[0].content.controls[2].opacity = 1
                    self.update()
            else:
                self.controls[0].content.controls[2].offset = transform.Offset(0.5, 0)
                self.controls[0].content.controls[2].opacity = 0
                self.update()
        else:
            pass


    def build(self):
        return Container(
            width=320,
            height=40,
            border=border.all(0.5, "white54"),
            bgcolor=self.bg_color,
            border_radius=25,
            content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        offset=[0.5,0,0,0],
                        name=self.icon_name,
                        size=16,
                        opacity=0.85
                    ),
                    TextField(
                        border_color="transparent",
                        bgcolor="#3D4354",
                        height=22,
                        width=250,
                        text_style=TextStyle(size=14, font_family="Consolas"),
                        content_padding=2,
                        cursor_color="black",
                        hint_text=self.text_hint,
                        hint_style=TextStyle(size=14, font_family="Consolas"),
                        password=self.hide,
                        on_change=lambda e: self.get_prefix_email(e),
                        on_blur=None
                    ),
                    self.prefix_email_containers(),
                ]
            )
        )

def main(page : Page):
    # Dimension
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = '#1B202D'
    page.fonts = {
        "Poppins": "fonts/Poppins/Poppins-Bold.ttf",
        "Mulish": "fonts/Mulish/Mulish-VariableFont_wght.ttf"
    }

    def highlight_link(e):
        e.control.style.color = colors.BLUE
        e.control.update()

    def unhighlight_link(e):
        e.control.style.color = None
        e.control.update()

    # Loop for animation box
    def animate_box():
        # Variable for animate box
        clock_wise_rotate = pi/4
        counter_clock_wise_rotate = -pi*2
        box_1 = page.controls[0].content.controls[1].controls[0].controls[0]
        box_2 = page.controls[0].content.controls[1].controls[1].controls[0]

        # Reverse rotation direction
        counter = 0
        while True:

            # Rotate 4x before switch direction
            if counter >= 0 and counter <= 4:

                # Update rotation box position
                box_1.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                box_2.rotate = transform.Rotate(
                    clock_wise_rotate, alignment.center
                )

                # Update transformation position rotation box
                box_1.update()
                box_2.update()

                # Update rotation value position
                clock_wise_rotate += pi/2
                counter_clock_wise_rotate -= pi/2

                counter += 1
                time.sleep(0.7)

            # Reverse rotation after 4x rotate
            if counter >= 5 and counter <= 10:
                # Update rotation value position
                clock_wise_rotate -= pi/2
                counter_clock_wise_rotate += pi/2

                # Update rotation box position
                box_1.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                box_2.rotate = transform.Rotate(
                    clock_wise_rotate, alignment.center
                )

                # Update transformation position rotation box
                box_1.update()
                box_2.update()

                counter += 1
                time.sleep(0.7)

            # Reset counter after 10 rotation to default
            if counter > 10:
                counter = 0

    # Main Page Controls
    page.add(
        Card(
            color="#1B202D",
            width=408,
            height=612,
            elevation=15,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=(
                    # Margin divider from card box for rotation box
                    Divider(height=40, color='transparent'),
                    # This is where the main controls will be added
                    Stack(
                        controls=[
                            AnimationBox("#e9665a", None, 0),
                            AnimationBox("#7df6dd", "#23262a", pi / 4)
                        ]
                    ),
                    # Margin divider from rotation box for title
                    Divider(height=20, color='transparent'),
                    Column(
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            # Title for sign up page
                            Text("Sign up", size=22, weight="bold", font_family="Consolas"),
                            # Margin divider from title for input field
                            Divider(height=20, color='transparent'),
                            Text("Username", size=20, weight="bold", font_family="Consolas"),
                            InputField("#3D4354", icons.PERSON_ROUNDED, "Email", False, True),
                            Divider(height=5, color='transparent'),
                            Text("Password", size=20, weight="bold", font_family="Consolas"),
                            InputField("#3D4354", icons.LOCK_OPEN_ROUNDED, "Password", True, False),
                            Divider(height=2, color='transparent'),
                            Row(
                                width=320,
                                alignment=MainAxisAlignment.END,
                                spacing=0,
                                controls=[
                                    Text("Already have account? ", size=15, font_family="Consolas"),
                                    Text(
                                        disabled=False,
                                        spans=[
                                            TextSpan(
                                                "Sign In",
                                                TextStyle(
                                                    decoration=TextDecoration.UNDERLINE,
                                                    size=15,
                                                    font_family="Consolas"
                                                ),
                                                on_click=lambda e: print(f"Clicked span: {e.control.uid}"),
                                                on_enter=highlight_link,
                                                on_exit=unhighlight_link,
                                                url="https://google.com"
                                            ),
                                        ],
                                    )
                                ]
                            ),
                            Divider(height=45, color='transparent'),
                            SignInButton('Sign Up')
                        ]
                    ),
                )
            )
        )
    )

    page.update()
    animate_box()


if __name__ == "__main__":
    flet.app(target=main, assets_dir='assets', view=WEB_BROWSER)