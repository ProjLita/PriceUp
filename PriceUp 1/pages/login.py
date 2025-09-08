import flet as ft

def login(page: ft.Page):
        page.padding = 0
        bgcolor = "#041c33"
        page.bgcolor = bgcolor
        


        # Título
        titulo = ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=90,
                controls=[
                    ft.Text("Bem Vindo", size=28, text_align=ft.TextAlign.CENTER),
                ]
            )
        )

        # Botão para entrar na tela inicial
        entrar = ft.ElevatedButton(
        content=ft.Text("Entrar", size=17, color=bgcolor, width=200, text_align=ft.TextAlign.CENTER),
        on_click=lambda e: e.page.go("/home"),
        style=ft.ButtonStyle(
                bgcolor="#198123",
                shape=ft.RoundedRectangleBorder(radius=15),
                
            )
        )
    
        # Botão para criar conta
        criar_conta = ft.ElevatedButton(
            content=ft.Text("Criar Conta", size=17, color=bgcolor, width=200, text_align=ft.TextAlign.CENTER),
            on_click=lambda e: e.page.go("/login3"),
            style=ft.ButtonStyle(
                    bgcolor=ft.Colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=15),
                    
                )
            )


        # Container principal 
        base = ft.Container(
            bgcolor="#003974",
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
                                     ft.Column(
                                        controls=[
                                        ft.Text("Email"),
                                        ft.TextField(hint_text="exemplo@exemplo.com", width=300, border_radius=10, fill_color="white", content_padding=20, height=40, color="black" ),
                                        ], spacing=1
                                    ),
                                    ft.Column(
                                        controls=[
                                        ft.Text("Senha"),
                                        ft.TextField(label="", width=300, border_radius=10, fill_color="white", content_padding=20, height=40, can_reveal_password=True, password=True, color="black"), # Falta add suffix=icon_button, mas não está pegando                            
                                        ],spacing=1
                                    ),   
                                        ]
                            ), 
                            ft.Column(
                                controls=[
                                    entrar,
                                    criar_conta
                                ]
                            )
                        ],
                        spacing=170,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                ],
            )
        )


        # Inserindo os elementos na tela
        return ft.View( route="/login", bgcolor=bgcolor, controls=[titulo, base])

