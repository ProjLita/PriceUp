import flet as ft

class login2(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0
        self.bgcolor = "#04043F"
        self.page.bgcolor = self.bgcolor
        self.container_color = "#003974"

        # logo = ft.Image(
        #     src="assets/price1.png", 
        #     width=100,
        #     height=100,
        # )

        self.titulo = ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=90,
                controls=[
                    ft.Text("Bem Vindo", size=28, text_align=ft.TextAlign.CENTER),
                ]
            )
        )

        entrar = ft.ElevatedButton(
        content=ft.Text("Editar", size=17, color="#04043F", width=200, text_align=ft.TextAlign.CENTER),
        style=ft.ButtonStyle(
                bgcolor="#198123",
                shape=ft.RoundedRectangleBorder(radius=15),
                
            )
        )
    
        google = ft.ElevatedButton(
            content=ft.Row(
                controls=[
                ft.Image(src="assets/Google.png"),
                ft.Text("Entrar com Google", size=17, color="#04043F", width=200, text_align=ft.TextAlign.CENTER),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                style=ft.ButtonStyle(bgcolor=ft.Colors.WHITE, shape=ft.RoundedRectangleBorder(radius=15),
                
                )
            ),
            
        

        self.base = ft.Container(
            bgcolor=self.container_color,
            height=page.height * 4.15,
            #width=200,
            border_radius=45,
            padding=40,
            content=ft.Row(
                spacing=2,
                alignment=ft.MainAxisAlignment.CENTER,
                #horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ 
                    ft.Column(
                        controls=[
                            ft.Column(
                                controls=[
                                ft.Text("Email"),
                                ft.TextField(label="exemplo@exemplo.com", width=300, border_radius=45, fill_color="white", content_padding=20, height=40),
                                ]
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Senha"),
                                ft.TextField(label="", width=300, border_radius=45, fill_color="white", content_padding=20, height=40),
                            
                                ]
                            ),
                             ft.Column(
                                controls=[
                                    entrar,
                                    google
                                ],
                                #horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ]
                    ),
                ],
            )
        )

    def build(self):
        self.page.add(ft.Column(
            expand=True,
            auto_scroll=True,
            controls=[
                # logo,
                self.titulo,
                self.base
            ]
        ))

        return self.page.add    

#ft.app(target=login2)
