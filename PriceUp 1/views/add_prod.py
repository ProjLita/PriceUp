import flet as ft

class Add_Sales(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0
        self.bgcolor = "#04043F"
        self.page.bgcolor = self.bgcolor
        self.container_color = "#003974"

        self.sugestoes = ft.Column()  # armazenar sugestões dinamicamente

        def selecionar_complemento(valor):
            campo_complemento.value = valor
            self.sugestoes.controls.clear()
            page.update()

        def atualizar_sugestoes(e):
            self.sugestoes.controls.clear()
            texto = campo_complemento.value.lower()
            for opcao in opcoes_complemento:
                if texto in opcao.lower():
                    self.sugestoes.controls.append(
                        ft.TextButton(
                            text=opcao,
                            on_click=lambda ev, o=opcao: selecionar_complemento(o)
                        )
                    )
            page.update()


        opcoes_complemento = ["Bolo de pote", "Brigadeiro", "Beijinho", "Goiabada", "Cocada"]

        campo_complemento = ft.TextField(
        label="Complemento",
        hint_text="Digite ou selecione um complemento",
        on_change=atualizar_sugestoes
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

        add = ft.ElevatedButton(
        content=ft.Text("Adicionar", size=17, color=self.bgcolor, width=170, text_align=ft.TextAlign.CENTER),
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
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                ft.Text("Imagem"),
                                ft.TextField(label="", border_radius=10, width=300, fill_color="white", content_padding=20, height=40, 
                                             suffix=ft.IconButton(icon=ft.Icons.DOWNLOAD)),
                                ], spacing=1
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Produto"),
                                ft.TextField(hint_text="Selecione o produto", border_radius=10, width=300, fill_color="white", content_padding=20, height=40),
                                campo_complemento,
                                self.sugestoes                           
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
                                    add
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

ft.app(target=Add_Sales)
