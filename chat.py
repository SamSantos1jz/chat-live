
import flet as ft


def main(page):
    text_title = ft.Text("Chat Ao Vivo")

    chat = ft.Column()

    user_name = ft.TextField(label="Digite seu nome:")    
    
    def send_msg_tunnel(mesage):
        type_msg = mesage["type_msg"]

        if type_msg == "mesage":
            text_msg_input = mesage["text_input"]
            user_msg = mesage["username"]

            chat.controls.append(ft.Text(f"{user_msg}: {text_msg_input}"))
        else:
             user_msg = mesage["username"]
             chat.controls.append(ft.Text(f"{user_msg} entrou no chat",
                                            size=12, italic=True,
                                            color=ft.colors.RED_ACCENT_700))
        page.update()
        
    page.pubsub.subscribe(send_msg_tunnel)

    def send_msg(event):
        page.pubsub.send_all({"text_input": text_msg.value, "username": user_name.value, 
                              "type_msg":"mesage"})
        text_msg.value = ""
        page.update()
        
    
    text_msg = ft.TextField(label="Digite uma mensagem", on_submit=send_msg)
    button_send_msg = ft.ElevatedButton("Enviar", on_click=send_msg)

    def enter_popup(event):

        page.pubsub.send_all({"username": user_name.value, "type_msg":"join"})
        page.add(chat)

        popup.open=False
        
        page.remove(button_init)
        
        page.add(ft.Row(
            [text_msg, button_send_msg]
        ))
        page.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao chat ao vivo"),
        content=user_name,
        actions=[ft.ElevatedButton("Entrar", on_click=enter_popup)]
    )

    def init_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()
        

    button_init = ft.ElevatedButton("Iniciar CHAT", on_click=init_chat)
    
    page.add(text_title)
    page.add(button_init)
    

ft.app(target=main, view=ft.WEB_BROWSER)

