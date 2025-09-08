import flet as ft

def homeView(page: ft.Page):
    bgcolor = "#041c33"
    container_color = "#003974"
    text_color = "#3ABF42"


    # Título
    titulo = ft.Container(
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


    # Balanço
    balanco = ft.Container(
        padding=ft.padding.only(left=10, right=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.Column(
                    controls=[
                        ft.Text("Balanço Total", size=20),
                        ft.Text("2,783.00$", weight=ft.FontWeight.BOLD, size=30)
                    ]
                ),
                ft.Container(width=1, height=70, bgcolor=ft.Colors.WHITE),
                ft.Column(
                    controls=[
                        ft.Text("Gastos Totais", size=20),
                        ft.Text("-987.40$", weight=ft.FontWeight.BOLD, size=30, color=text_color)
                    ]
                ),
            ]
        )
    )


    # Primeiro botão do container (com carrinho)
    poup_metas= ft.ElevatedButton(
        bgcolor=bgcolor,
        expand=True,
        height=110,
        width=page.width * 0.29,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                content=ft.Row(
                            controls=[
                                ft.Column(
                                    alignment=ft.MainAxisAlignment.START,  # Alinha os elementos no topo
                                    spacing=-5,  # Aproxima a imagem dos textos
                                    controls=[
                                        ft.Image(src="assets/Car.png", width=70, height=70),
                                        ft.Column(
                                            spacing=0,
                                            controls=[
                                                ft.Container(
                                                    padding=ft.padding.only(left=7),
                                                    content=ft.Column( 
                                                        spacing=0,
                                                        controls=[
                                                            ft.Text("Poupança", size=10, color=text_color),
                                                            ft.Text("Em Metas", size=10, color=text_color)
                                                        ]
                                                    )
                                                )
                                            ]
                                        ),
                                    ]
                                ),
                                ft.Container(width=1, height=70, bgcolor=ft.Colors.WHITE),
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Image(src="assets/Salary.png" , height=40, width=40),
                                                ft.Column(
                                                    controls=[
                                                    ft.Text("Receita na última semana", size=12, color=text_color),
                                                    ft.Text("$650.00", weight=ft.FontWeight.BOLD, size=15, color=text_color),
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
                                                                ft.Text("Alimentação na semana passada",  size=12, color=text_color),
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
    

    # Botões de frequencia (diário, semanal, mensal)
    freq = ft.Container(
        bgcolor=bgcolor,
        height=page.height * 0.08,
        border_radius=15,
        padding=ft.padding.only(left=15, right=15),
        alignment=ft.alignment.center,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.ElevatedButton(
                    expand=True,
                    content=ft.Text("Diário", size=17, color=bgcolor),
                    style=ft.ButtonStyle(bgcolor="#2AA736", shape=ft.RoundedRectangleBorder(radius=10)),
                ),
                ft.ElevatedButton(
                    expand=True,
                    content=ft.Text("Semanal", size=17, color=bgcolor),
                    style=ft.ButtonStyle(bgcolor="#2AA736", shape=ft.RoundedRectangleBorder(radius=10)),
                ),
                ft.ElevatedButton(
                    expand=True,
                    content=ft.Text("Mensal", size=17, color=bgcolor),
                    style=ft.ButtonStyle(bgcolor="#2AA736", shape=ft.RoundedRectangleBorder(radius=10)),
                ),
            ]
        ),
        width=page.width * 0.29
    )


    # Status de venda, compra e estoque
    sub_parte = ft.Container(
        bgcolor=container_color,
        padding=-5,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.Row(
                    controls=[
                        ft.Image(src="assets/IconSalary.png", width=80, height=80),
                        ft.Column(
                            controls=[
                                ft.Text("Recebido", size=15),
                                ft.Text("18:27 - 30/Abril", size=14, color=text_color),
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
                                ft.Text("7:00 - 25/Abril", size=14, color=text_color),
                            ],
                            spacing=-1
                        ),
                        ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                        ft.Text("Estoque", size=17),
                        ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                        ft.Text("-100,00$", size=20, color=text_color)
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Image(src="assets/IconGroceries.png", width=80, height=80),
                        ft.Column(
                            controls=[
                                ft.Text("Mercado", size=15),
                                ft.Text("8:30 - 15/Abril", size=14, color=text_color),
                            ],
                            spacing=-1
                        ),
                        ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                        ft.Text("Estoque", size=17),
                        ft.Container(width=1.5, height=40, bgcolor="#3E6FA4"),
                        ft.Text("-674,40$", size=20, color=text_color)
                    ]
                )
            ]

        )
    )

    # Base do layout
    base = ft.Container(
        bgcolor=container_color,
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

    return ft.View(
        route="/home",
        padding=ft.padding.only(bottom=80), 
        controls=[
            titulo,
            balanco,
            base,
        ],
        bgcolor=bgcolor
    )
