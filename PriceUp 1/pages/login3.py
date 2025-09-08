import flet as ft

def login3(page: ft.Page):
        page.padding = 0
        bgcolor = "#04043F"
        page.bgcolor = bgcolor
        container_color = "#003974"


        titulo = ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=90,
                controls=[
                    ft.Text("Crie Sua Conta", size=28, text_align=ft.TextAlign.CENTER),
                ]
            )
        )

        confirmar = ft.ElevatedButton(
        content=ft.Text("Confirmar", size=17, color="#04043F", width=200, text_align=ft.TextAlign.CENTER),
        on_click=lambda e: e.page.go("/login"),
        style=ft.ButtonStyle(
                bgcolor="#198123",
                shape=ft.RoundedRectangleBorder(radius=15),
                
            )
        )


        base = ft.Container(
            bgcolor=container_color,
            height=page.height * 4.15,
            border_radius=45,
            padding=40,
            content=ft.Row(
                spacing=2,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ 
                    ft.Column(
                        controls=[
                            ft.Column(
                                controls=[
                                ft.Text("Nome Completo"),
                                ft.TextField(label="", width=300, border_radius=8, fill_color="white", content_padding=20, height=40, color="black"),
                                ]
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Email"),
                                ft.TextField(hint_text="exemplo@exemplo.com", width=300, border_radius=8, fill_color="white", content_padding=20, height=40, color="black"),
                                ]
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Número De Telefone"),
                                ft.TextField(hint_text="12 3456-7890", width=300, border_radius=8, fill_color="white", content_padding=20, height=40, color="black"),
                            
                                ]
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Data De Nascimento"),
                                ft.TextField(hint_text="DD / MM / YY", width=300, border_radius=8, fill_color="white", content_padding=20, height=40, color="black"),
                                ]
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Senha"),
                                ft.TextField(label="", width=300, border_radius=8, fill_color="white", content_padding=20, can_reveal_password=True, password=True, height=40, color="black"),
                            
                                ]
                            ),
                             ft.Column(
                                controls=[
                                    confirmar
                                ],
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                ],
            )
        )

        return ft.View( route="/login3", bgcolor=bgcolor, controls=[titulo, base])

