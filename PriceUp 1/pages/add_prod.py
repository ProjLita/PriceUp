import flet as ft

def Add_Sales(self, page: ft.Page):
        page.padding = 0
        bgcolor = "#041c33"
        page.bgcolor = bgcolor
        container_color = "#003974"

        sugestoes = ft.Column()  # armazenar sugestões dinamicamente

        def selecionar_complemento(valor):
            campo_complemento.value = valor
            sugestoes.controls.clear()
            page.update()

        def atualizar_sugestoes(e):
            sugestoes.controls.clear()
            texto = campo_complemento.value.lower()
            for opcao in opcoes_complemento:
                if texto in opcao.lower():
                    sugestoes.controls.append(
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

        add = ft.ElevatedButton(
        content=ft.Text("Adicionar", size=17, color=bgcolor, width=170, text_align=ft.TextAlign.CENTER),
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
                                sugestoes                           
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

        return ft.View( route="/add_prod", expand=True, auto_scroll=True, controls=[titulo, base])

