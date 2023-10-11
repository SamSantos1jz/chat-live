import flet as ft


def main(page):
    text_title = ft.Text("ChatTESTE")
    
    def init_chat(event):
        text_enter = ft.Text("Entrou no CHAT")
        page.add(text_enter)

    button_init = ft.ElevatedButton("Iniciar CHAT", on_click=init_chat)
    
    page.add(text_title)
    page.add(button_init)
    

ft.app(target=main, view=ft.WEB_BROWSER)

