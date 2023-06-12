from router import *

def main(page : Page):
    # Dimension
    page.title = "ChatKui"
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = '#1B202D'
    page.fonts = {
        "Poppins": "fonts/Poppins/Poppins-Bold.ttf",
        "Mulish": "fonts/Mulish/Mulish-VariableFont_wght.ttf"
    }

    myRouter = Router(page)
    page.on_route_change = myRouter.route_change

    page.add(myRouter.body)
    # myRouter.animate_box()
    page.update()

if __name__ == "__main__":
    flet.app(port=8550, target=main, assets_dir='assets', view=WEB_BROWSER)