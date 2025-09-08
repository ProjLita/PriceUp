import flet as ft

def Edit_Sales(self, page: ft.Page):
        page.padding = 0
        bgcolor = "#041c33"
        page.bgcolor = bgcolor
        container_color = "#003974"


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

        titulo = ft.Container(
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
        content=ft.Text("Salvar", size=17, color=bgcolor, width=170, text_align=ft.TextAlign.CENTER),
        style=ft.ButtonStyle(
                bgcolor="#198123",
                shape=ft.RoundedRectangleBorder(radius=7),
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

        return ft.View( route="/edit_sale", expand=True, auto_scroll=True, controls=[titulo, base])

