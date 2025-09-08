import flet as ft
import threading
import time

def main(page: ft.Page):
    page.bgcolor = "#021A35"
    page.window_width = 400
    page.window_height = 800
    page.title = "Price Up"

    # Logo centralizada inicialmente
    logo_container = ft.Container(
        content=ft.Image(src="assets/logo.png", width=250),
        offset=ft.Offset(0, 0),  # começa no centro
        animate_offset=ft.Animation(duration=700, curve=ft.AnimationCurve.EASE_IN_OUT),
        alignment=ft.alignment.center_right,
        width=page.window_width,
        height=page.window_height,
    )

    # Container dos botões (inicialmente invisível)
    botoes_container = ft.Column(
        [
            ft.Text(
                "Garanta sua tranquilidade e gerencie suas finanças",
                size=16,
                color="white",
                text_align=ft.TextAlign.CENTER,
            ),
            ft.ElevatedButton(
                text="Entrar",
                bgcolor="#00C853",
                color="white",
                width=200,
                on_click=lambda e: print("Entrar clicado"),
            ),
            ft.ElevatedButton(
                text="Criar Conta",
                bgcolor="#FFFFFF",
                color="black",
                width=200,
                on_click=lambda e: print("Criar Conta clicado"),
            ),
        ],
        visible=False,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    # Posicionar os botões no centro da tela (com Stack)
    botoes_overlay = ft.Container(
        content=botoes_container,
        alignment=ft.alignment.center,
        width=page.window_width,
        height=page.window_height,
    )

    # Usar Stack para sobrepor elementos
    layout = ft.Stack(
        [logo_container, botoes_overlay],
        # alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(layout)

    # Animação da logo e exibição dos botões
    def animar():
        time.sleep(1)  # espera inicial
        logo_container.offset = ft.Offset(0, -0.3)  # sobe suavemente
        page.update()

        time.sleep(0.8)
        botoes_container.visible = True
        page.update()

    threading.Thread(target=animar).start()

ft.app(target=main)
