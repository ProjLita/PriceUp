import flet as ft

class homeView(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0
        self.bgcolor = "#04043F"
        self.page.bgcolor = self.bgcolor
        self.container_color = "#003974"
        self.text_color = "#3ABF42"


        # Título
        self.titulo = ft.Container(
            padding=ft.padding.only(left=15),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=90,
                controls=[ 
                        ft.Row(
                            controls=[
                                ft.Text("Olá!", size=17, text_align=ft.TextAlign.START),
                                ft.IconButton(icon=ft.Icons.HELP_OUTLINE, width=60, height=60)
                            ]
                        ),  
                        ft.Text("Bem vindo de volta", size=17, text_align=ft.TextAlign.START),                        
                ],
                spacing=-50
            )
        )

        # Informações iniciais a baixo do título
        balanco = ft.Container(
            padding=ft.padding.only(left=10, right=10),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Balanço Total", size=20)
                                    ]
                                ),
                                ft.Text("2,783.00$", weight=ft.FontWeight.BOLD, size=30)
                            ], 
                            spacing=2
                        ),
                        ft.Container(width=1, height=70, bgcolor=ft.Colors.WHITE),
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Gastos Totais", size=20)
                                    ]
                                ),
                                ft.Text("-987.40$", weight=ft.FontWeight.BOLD, size=30, color=self.text_color)
                            ], spacing=2
                        ),
                    ],
                )
            )


        # Primeiro botão do container (com carrinho)
        poup_metas= ft.ElevatedButton(
            bgcolor=self.bgcolor,
            expand=True,
            height=110,
            width=page.width * 0.29,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                    content=ft.Row(
                                controls=[
                                    ft.Column(
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                        controls=[
                                            ft.Image(src="assets/Car.png", width=70, height=70),
                                            ft.Column(
                                                controls=[
                                                    ft.Text("Poupança", size=10, color=self.text_color),
                                                    ft.Text("Em Metas", size=10, color=self.text_color)
                                                ],
                                                spacing=1
                                            ),
                                        ],
                                        spacing=-3
                                    ),
                                    ft.Container(width=1, height=70, bgcolor=ft.Colors.WHITE),
                                    ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Image(src="assets/Salary.png" , height=40, width=40),
                                                    ft.Column(
                                                        controls=[
                                                        ft.Text("Receita na última semana", size=12, color=self.text_color),
                                                        ft.Text("$650.00", weight=ft.FontWeight.BOLD, size=15, color=self.text_color),
                                                        ],
                                                        spacing=1
                                                    ),
                                                ]
                                                
                                            ),
                                            ft.Container(width=170 , height=1, bgcolor=ft.Colors.WHITE),
                                            ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        controls=[
                                                            ft.Image(src="assets/Food.png", height=40, width=40),
                                                            ft.Column(
                                                                controls=[
                                                                    ft.Text("Alimentação na semana passada",  size=12, color=self.text_color),
                                                                    ft.Text("-$100.00", weight=ft.FontWeight.BOLD, size=15, color="#0E2DB9")
                                                                ], 
                                                                spacing=1
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=5
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,                        
                                spacing=5
                            ),
                        )


        # Status de venda, compra e estoque
        sub_parte = ft.Container(
            bgcolor=self.container_color,
            padding=-5,
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Image(src="assets/IconSalary.png", width=80, height=80),
                            ft.Column(
                                controls=[
                                    ft.Text("Recebido", size=15),
                                    ft.Text("18:27 - 30/Abril", size=14, color=self.text_color),
                                ],
                                spacing=-1
                            ),
                            ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                            ft.Text(" Diário ", size=17),
                            ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                            ft.Text(" 20,00$", size=20)
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Image(src="assets/IconGroceries.png", width=80, height=80),
                            ft.Column(
                                controls=[
                                    ft.Text("Mercado", size=15),
                                    ft.Text("7:00 - 25/Abril", size=14, color=self.text_color),
                                ],
                                spacing=-1
                            ),
                            ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                            ft.Text("Estoque", size=17),
                            ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                            ft.Text("-100,00$", size=20, color=self.text_color)
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Image(src="assets/IconGroceries.png", width=80, height=80),
                            ft.Column(
                                controls=[
                                    ft.Text("Mercado", size=15),
                                    ft.Text("8:30 - 15/Abril", size=14, color=self.text_color),
                                ],
                                spacing=-1
                            ),
                            ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                            ft.Text("Estoque", size=17),
                            ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                            ft.Text("-674,40$", size=20, color=self.text_color)
                        ]
                    )
                ]

            )
        )

        # Botões de frequencia (diário, semanal, mensal)
        freq = ft.Container(
            bgcolor=self.bgcolor,
            height=page.height * 0.08,
            border_radius= 15,
            padding= ft.padding.only(left=15, right=15),
            content=ft.Row(
                expand=True,
                controls=[
                    ft.ElevatedButton(
                            content=ft.Text("Diário", size=17, color=self.bgcolor, width=90, text_align=ft.TextAlign.CENTER),
                            style=ft.ButtonStyle(bgcolor="#2AA736", shape=ft.RoundedRectangleBorder(radius=10),)
                    ),
                     ft.ElevatedButton(
                            content=ft.Text("Semanal", size=17, color=self.bgcolor, width=90, text_align=ft.TextAlign.CENTER),
                            style=ft.ButtonStyle(bgcolor="#2AA736", shape=ft.RoundedRectangleBorder(radius=10),)
                    ),
                     ft.ElevatedButton(
                            content=ft.Text("Mensal", size=17, color=self.bgcolor, width=90, text_align=ft.TextAlign.CENTER),
                            style=ft.ButtonStyle(bgcolor="#2AA736", shape=ft.RoundedRectangleBorder(radius=10),)
                    )                            
                ]
            )
        )

        # Contaniner principal
        self.base = ft.Container(
            bgcolor=self.container_color,
            height=page.height * 1.15,
            border_radius=45,
            padding=ft.padding.only(left=20, right=20, top=20),
            content=ft.Row(
                expand=True,
                spacing=2,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ 
                    ft.Column(
                        controls=[
                            ft.Column(
                                controls=[
                                    poup_metas,
                                    freq,
                                    sub_parte
                                ]
                            )
                        ]
                    ),
                ],
            )
        )

        # Inserção dos objetos
        self.page.add(ft.Column(
            expand=True,
            auto_scroll=True,
            controls=[
                self.titulo,
                balanco,
                self.base
            ]
        ))

ft.app(target=homeView)
