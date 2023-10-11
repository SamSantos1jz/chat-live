import flet as ft


def main(page):
    text_title = ft.Text("Chat Ao Vivo")
    
    user_name = ft.TextField()    

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao chat ao vivo"),
        content=user_name,
        actions=[ft.ElevatedButton("Entrar")]
    )

    def init_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()
        

    button_init = ft.ElevatedButton("Iniciar CHAT", on_click=init_chat)
    
    page.add(text_title)
    page.add(button_init)
    

ft.app(target=main, view=ft.WEB_BROWSER)

