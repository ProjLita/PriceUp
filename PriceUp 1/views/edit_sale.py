import flet as ft

class Edit_Sales(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0
        self.bgcolor = "#04043F"
        self.page.bgcolor = self.bgcolor
        self.container_color = "#003974"


        # descricao = ft.TextField(
        #     hint_text="Inserir Descrição (Pago Em Dinheiro)",
        #     multiline=True,
        #     min_lines=1,
        #     max_lines=10,
        #     width=300, 
        #     fill_color="white", 
        #     border_radius=10
        # )

        descricao = ft.TextField(
            label="",
            hint_text="Inserir Descrição (Pago Em Dinheiro)",
            multiline=True,
            min_lines=5,
            max_lines=10,
            width=300,
            fill_color="white",
            border_radius=10,
            text_style=ft.TextStyle(color=ft.Colors.GREEN_900),
        )

        self.titulo = ft.Container(
            padding=ft.padding.only(left=15),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=90,
                controls=[ 
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.IconButton(icon=ft.Icons.ARROW_BACK, width=60, height=60),
                                ft.Text("Adicionar Produto", size=17, text_align=ft.TextAlign.START),
                                ft.IconButton(icon=ft.Icons.HELP_OUTLINE, width=60, height=60)
                            ]
                        ),                 
                    ]
                )
            )

        save = ft.ElevatedButton(
        content=ft.Text("Salvar", size=17, color=self.bgcolor, width=170, text_align=ft.TextAlign.CENTER),
        style=ft.ButtonStyle(
                bgcolor="#198123",
                shape=ft.RoundedRectangleBorder(radius=7),
            )
        )

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
                                ft.Text("Data"),
                                ft.TextField(label="", border_radius=10, width=300, fill_color="white", content_padding=20, height=40, 
                                             suffix=ft.IconButton(icon=ft.Icons.CALENDAR_MONTH)),
                                ], spacing=1
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Produto"),
                                ft.TextField(hint_text="Selecione o produto", border_radius=10, width=300, fill_color="white", content_padding=20, height=40),                           
                                ], spacing=1
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Valor"),
                                ft.TextField(label="", border_radius=10, width=300, fill_color="white", content_padding=20, height=40),
                                ], spacing=1
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Quatidade"),
                                ft.TextField(label="", border_radius=10, width=300, fill_color="white", content_padding=20, height=40),
                                ], spacing=1
                            ),
                            ft.Column(
                                controls=[
                                    descricao
                                ], spacing=1
                            ),
                             ft.Column(
                                controls=[
                                    save
                                ],
                            ),
                        ]
                    ),
                ],
            )
        )

        self.page.add(ft.Column(
            expand=True,
            auto_scroll=True,
            controls=[
                self.titulo,
                self.base
            ]
        ))

ft.app(target=Edit_Sales)
