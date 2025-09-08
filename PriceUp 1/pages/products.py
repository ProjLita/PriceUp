import flet as ft

def ProdView(self, page: ft.Page):
        page.padding = 0
        bgcolor = "#041c33"
        page.bgcolor = bgcolor
        container_color = "#003974"
        text_color = "#3ABF42"


        titulo = ft.Container(
            padding=ft.padding.only(bottom=-20),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=90,
                controls=[ 
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.IconButton(icon=ft.Icons.ARROW_BACK, width=60, height=60),
                                ft.Text("Meus Produtos", size=17, text_align=ft.TextAlign.START),
                                ft.IconButton(icon=ft.Icons.HELP_OUTLINE, width=60, height=60)
                            ]
                        ),                 
                    ]
                )
            )
        
        # Nome do Produto
        titulo2 = ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
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

        # Botões de produtos (sabores e add)
        prod1 = ft.FloatingActionButton(bgcolor="#2AA736", shape=ft.RoundedRectangleBorder(radius=20), height=100, width=100, text=" ")
        prod2 = ft.FloatingActionButton(bgcolor="#84D2EE", shape=ft.RoundedRectangleBorder(radius=20), height=100, width=100, text=" ")
        prod3 = ft.FloatingActionButton(bgcolor="#0068FF", shape=ft.RoundedRectangleBorder(radius=20), height=100, width=100, text=" ")
        add = ft.FloatingActionButton(bgcolor="#84D2EE", shape=ft.RoundedRectangleBorder(radius=20), height=100, width=100, icon=ft.Icons.ADD)


        # Contaniner principal
        base = ft.Container(
            bgcolor=container_color,
            height=page.height * 1.15,
            border_radius=45,
            padding=ft.padding.only(left=20, right=20, top=-410),
            content=ft.Column(
                controls=[ 
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Column(
                                controls=[prod1,ft.Text("Brigadeiro", size=12)],
                            ),
                            ft.Column(
                                controls=[prod2,ft.Text("Morango", size=12)]
                            ),
                            ft.Column(
                                controls=[prod1,ft.Text("Leite Ninho", size=12)]
                            ),
                        ],
                        spacing=20
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(
                            controls=[ prod3,ft.Text("Dois Amores", size=12)]
                            ),
                            ft.Column(
                                controls=[add,ft.Text("Adicionar", size=12)]
                            ),
                        ],
                        spacing=20
                    )
                    ]
                ),
            )
        
        # Inserção dos objetos
        # page.add(ft.Column(
        #             alignment=ft.alignment.center,
        #             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #             expand=True,
        #             auto_scroll=True,
        #             controls=[
        #                 titulo,
        #                 titulo2,
        #                 balanco,
        #                 base
        #             ],
        #             spacing=30,
        #         )
        #     )

        return ft.View( route="products", controls=[titulo,titulo2, balanco, base], spacing=30)

