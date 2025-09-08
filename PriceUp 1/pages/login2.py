import flet as ft

def login2(page: ft.Page):  
        page.padding = 0
        bgcolor = "#041c33"
        page.bgcolor = bgcolor
        container_color = "#003974"
        

        titulo = ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=90,
                controls=[
                    ft.Text("Bem Vindo", size=28, text_align=ft.TextAlign.CENTER),
                ]
            )
        )

        entrar = ft.ElevatedButton(
            content=ft.Text("Entrar", size=17, color="#04043F", width=200, text_align=ft.TextAlign.CENTER),
            style=ft.ButtonStyle(bgcolor="#198123", shape=ft.RoundedRectangleBorder(radius=8)),
            on_click=lambda e: page.go("/home"),
        )
    
        google = ft.ElevatedButton(
            content=ft.Row(
                controls=[
                ft.Image(src="assets/Google.png"),
                ft.Text("Entrar com Google", size=15, color="#04043F", width=180, text_align=ft.TextAlign.CENTER),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                #vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                on_click=lambda e: e.page.go("/login3"),
                style=ft.ButtonStyle(bgcolor=ft.Colors.WHITE, shape=ft.RoundedRectangleBorder(radius=8),
                )
            )
            
        facebook = ft.ElevatedButton(
            content=ft.Row(
                controls=[
                ft.Image(src="assets/Facebook.png"),
                ft.Text("Entrar com Facebook", size=15, color="#04043F", width=170, text_align=ft.TextAlign.START),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                #vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                on_click=lambda e: e.page.go("/login3"),
                style=ft.ButtonStyle(bgcolor=ft.Colors.WHITE, shape=ft.RoundedRectangleBorder(radius=8),
                )
            )
        
        apple = ft.ElevatedButton(
            content=ft.Row(
                controls=[
                ft.Image(src="assets/Apple.png"),
                ft.Text("Entrar com Apple", size=15, color="#04043F", width=185, text_align=ft.TextAlign.CENTER),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                on_click=lambda e: e.page.go("/login3"),
                style=ft.ButtonStyle(bgcolor=ft.Colors.WHITE, shape=ft.RoundedRectangleBorder(radius=8),
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
                                    ft.Column(
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                ft.Text("Email"),
                                                ft.TextField(hint_text="exemplo@exemplo.com", width=300, border_radius=8, fill_color="white", content_padding=10, height=40, color="black"),
                                                ], spacing=1
                                            ),
                                            ft.Column(
                                                controls=[
                                                ft.Text("Senha"),
                                                ft.TextField(label="", width=300, border_radius=8, fill_color="white", can_reveal_password=True, password=True, content_padding=20, height=40, color="black"),
                                                ], spacing=1
                                            ),                                                
                                        ]
                                    ),
                                    ft.Column(
                                        controls=[
                                            entrar
                                        ]
                                    )
                                ],
                                spacing=40,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            ft.Column(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            google,
                                            facebook,
                                            apple
                                        ],
                                    ),
                                ]
                            )
                        ], 
                        spacing=110,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ]
            )
        )

        # def build(self):
        return ft.View( route="/login2", bgcolor=bgcolor, controls=[titulo, base])

