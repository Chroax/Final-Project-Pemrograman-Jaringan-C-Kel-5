from signin import *
from signup import *
from list_chat import *

class Router:
    # Loop for animation box
    def animate_box(self):
        # Variable for animate box
        clock_wise_rotate = pi / 4
        counter_clock_wise_rotate = -pi * 2
        box_1 = self.page.controls[0].content.content.controls[1].controls[0].controls[0]
        box_2 = self.page.controls[0].content.content.controls[1].controls[1].controls[0]
        print(self.page.route)
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
                box_2.update()
                box_1.update()

                # Update rotation value position
                clock_wise_rotate += pi / 2
                counter_clock_wise_rotate -= pi / 2

                counter += 1
                time.sleep(0.7)

            # Reverse rotation after 4x rotate
            if counter >= 5 and counter <= 10:
                # Update rotation value position
                clock_wise_rotate -= pi / 2
                counter_clock_wise_rotate += pi / 2

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

    def __init__(self, page):
        self.page = page
        self.routes = {
            "/sign-in": SignInView(page),
            "/sign-up": SignUpView(page),
            "/chat": ListChatView(page)
        }
        self.body = Container(content=self.routes['/sign-in'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()