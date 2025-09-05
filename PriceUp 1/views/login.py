import flet as ft

class login(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0
        self.bgcolor = "#04043F"
        self.page.bgcolor = self.bgcolor
        self.container_color = "#003974"
        show_password=False



        # def para funcionalidade do icone que permite a visibilidade da senha
        def password_view(e):
            nonlocal show_password
            show_password = not show_password
            #password_field.password = not show_password
            icon_button.icon = ft.Icons.VISIBILITY if not show_password else ft.Icons.VISIBILITY_OFF
            page.update()

            icon_button = ft.IconButton(icon=ft.Icons.VISIBILITY, on_click=password_view) #Icone para visualizar a senha


        # Título
        self.titulo = ft.Container(
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
        content=ft.Text("Editar", size=17, color=self.bgcolor, width=200, text_align=ft.TextAlign.CENTER),
        style=ft.ButtonStyle(
                bgcolor="#198123",
                shape=ft.RoundedRectangleBorder(radius=15),
                
            )
        )
    
        # Botão para criar conta
        criar_conta = ft.ElevatedButton(
            content=ft.Text("Criar Conta", size=17, color=self.bgcolor, width=200, text_align=ft.TextAlign.CENTER),
            style=ft.ButtonStyle(
                    bgcolor=ft.Colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=15),
                    
                )
            )

        # Container principal 
        self.base = ft.Container(
            bgcolor=self.container_color,
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
                                ft.Text("Email"),
                                ft.TextField(hint_text="exemplo@exemplo.com", width=300, border_radius=10, fill_color="white", content_padding=20, height=40, color="black" ),
                                ], spacing=1
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Senha"),
                                ft.TextField(label="", width=300, border_radius=10, fill_color="white", content_padding=20, height=40, can_reveal_password=False, password=True, color="black"), # Falta add suffix=icon_button, mas não está pegando                            
                                ],spacing=1
                            ),
                             ft.Column(
                                controls=[
                                    entrar,
                                    criar_conta
                                ],
                            ),
                        ]
                    ),
                ],
            )
        )


        # Inserindo os elementos na tela
        self.page.add(ft.Column(
            expand=True,
            auto_scroll=True,
            controls=[
                # logo,
                self.titulo,
                self.base
            ]
        ))

ft.app(target=login)
