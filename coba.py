import flet as ft
import os

ON_WEB = os.getenv("ONWEB") or "0"

def main(page):
    def btn_click(e):
        if not cmd.value:
            cmd.error_text = "masukkan command"
            page.update()
        else:
            txt = cmd.value
            lv.controls.append(ft.Text(f"command: {txt}"))
            cmd.value=""
            page.update()

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    cmd = ft.TextField(label="Your command")

    page.add(lv)
    page.add(cmd, ft.ElevatedButton("Send", on_click=btn_click))


if __name__=='__main__':
        ft.app(target=main,view=ft.WEB_BROWSER,port=8550)