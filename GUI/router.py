from signin import *
from signup import *
from list_chat import *
from chat_message import *

class Router:
    def __init__(self, page, cc):
        self.page = page
        self.routes = {
            "/sign-in": SignInView(page, cc),
            "/sign-up": SignUpView(page, cc),
            "/chat": ListChatView(page, cc),
            "/msgchat/afdal": ChatMessageView(page, cc,"afdal"),
            "/msgchat/anton": ChatMessageView(page, cc,"anton"),
            "/msgchat/cahyadi": ChatMessageView(page, cc,"cahyadi"),
            "/msgchat/ariq": ChatMessageView(page, cc,"ariq"),
            "/msgchat/marcel": ChatMessageView(page, cc,"marcel"),
            "/msgchat/frederick": ChatMessageView(page, cc,"frederick"),
        }
        self.body = Container(content=self.routes['/sign-in'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()