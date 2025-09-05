import flet as ft

class SalesView(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0
        self.bgcolor = "#04043F"
        self.page.bgcolor = self.bgcolor
        self.container_color = "#003974"
        self.text_color = "#3299FF"

        titulo = ft.Container(
            padding=ft.padding.only(left=15, bottom=-20),
            content=ft.Column(
                height=90,
                controls=[ 
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.IconButton(icon=ft.Icons.ARROW_BACK, width=60, height=60),
                                ft.Text("Vendas", size=17, text_align=ft.TextAlign.START),
                                ft.IconButton(icon=ft.Icons.HELP_OUTLINE, width=60, height=60)
                            ]
                        ),                 
                    ]
                )
            )
        
        titulo2 = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Image(src="assets/Cake.png"),
                    ft.Text("Bolo de pote", weight=ft.FontWeight.BOLD, size=30)
                ]
            )
        )
        

        balanco = ft.Container(
            padding=ft.padding.only(left=20, right=20),
                content=ft.Row(
                     alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Balanço Total", size=10)
                                    ]
                                ),
                                ft.Text("2,783.00$", weight=ft.FontWeight.BOLD, size=20)
                            ], 
                            spacing=2
                        ),
                        ft.Container(width=1, height=40, bgcolor=ft.Colors.WHITE),
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Gastos Totais", size=10)
                                    ]
                                ),
                                ft.Text("-987.40$", weight=ft.FontWeight.BOLD, size=20, color="#3299FF")
                            ], spacing=2
                        ),
                    ],
                )
            )

        add_vend = ft.ElevatedButton(
        content=ft.Text("Adicionar", size=17, color=self.bgcolor, width=170, text_align=ft.TextAlign.CENTER),
        style=ft.ButtonStyle(
                bgcolor="#198123",
                shape=ft.RoundedRectangleBorder(radius=7),
            )
        )

        self.base = ft.Container(
            bgcolor=self.container_color,
            height=page.height * 1.15,
            border_radius=45,
            padding=ft.padding.only(left=20, right=20, top=-410),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[ 
                    # ft.Row(
                    #     controls=[
                    #         ft.Text("Abril", size=12),
                    #         ft.Image(src="assets/Calendar.png", width=20, height=20)
                    #     ]       
                    # ),
                    ft.Row(
                        controls=[
                            ft.Image(src="assets/IconFood.png", width=80, height=80),
                            ft.Column(
                                controls=[
                                    ft.Text("Brigadeiro - 2x", size=15),
                                    ft.Text("18:27 - 15/Abril", size=14, color=self.text_color),
                                ],
                                spacing=-1
                            ),
                            ft.Text("-30,00$", size=17, text_align=ft.TextAlign.END)
                        ]
                    ),
                    ft.Row(
                        
                        controls=[
                            ft.Image(src="assets/IconFood.png", width=80, height=80),
                            ft.Column(
                                controls=[
                                    ft.Text("Brigadeiro - 2x", size=15),
                                    ft.Text("15:00 - 24/Abril", size=14, color=self.text_color),
                                ],
                                spacing=-1
                            ),
                            ft.Text("-16,50$", size=17, text_align=ft.TextAlign.END)
                        ]
                    ),
                    add_vend
                    ]
                ),
            )
        

        self.page.add(ft.Column(
                    alignment=ft.alignment.center,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    auto_scroll=True,
                    controls=[
                        titulo,
                        titulo2,
                        balanco,
                        self.base
                    ],
                    spacing=30,
                )
            )

ft.app(target=SalesView)
