# splash_screen.py
import flet as ft
import threading
import time

def splash_view(page: ft.Page):
    page.bgcolor = "#041c33"
    page.window_width = 400
    page.window_height = 800
    page.title = "Price Up"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    logo = ft.Container(
        content=ft.Image(src="assets/logo.png", width=250, ),
        offset=ft.Offset(0, 0),
        animate_offset=ft.Animation(700, curve=ft.AnimationCurve.EASE_IN_OUT),
        alignment=ft.alignment.center,
        width=page.window_width,
        height=page.window_height,
    )

    botoes = ft.Container(
        content=ft.Column(
            [
                ft.Text("Garanta sua tranquilidade e gerencie suas finanças",
                        size=16, color="white", text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    text="Entrar",
                    bgcolor="#39C041",
                    color="white",
                    width=200,
                    on_click=lambda e: page.go("/login2"),
                ),
                ft.ElevatedButton(
                    text="Criar Conta",
                    bgcolor="white",
                    color="black",
                    width=200,
                    on_click=lambda e: page.go("/login3"),
                ),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        opacity=0,
        offset=ft.Offset(0, 0.2),
        animate_opacity=ft.Animation(500),
        animate_offset=ft.Animation(500),
        alignment=ft.alignment.center,
        width=page.window_width,
        height=page.window_height,
    )

    layout = ft.Stack([logo, botoes], expand=True, alignment=ft.alignment.center)
    page.add(layout)

    def animate():
        time.sleep(1)
        logo.offset = ft.Offset(0, -0.3)
        page.update()
        time.sleep(0.8)
        botoes.opacity = 1
        botoes.offset = ft.Offset(0, 0)
        page.update()

    threading.Thread(target=animate).start()

    # Retorne a view como Container para o stack de views
    return ft.View("/splash_screen", bgcolor = "#041c33", controls=[layout])
