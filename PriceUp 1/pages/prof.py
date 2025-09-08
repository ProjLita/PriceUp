import flet as ft

def Profile(self, page: ft.Page):
        page.padding = 0
        bgcolor = "#041c33"
        page.bgcolor = bgcolor
        container_color = "#003974"

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
                                ft.Text("Editar Perfil", size=17, text_align=ft.TextAlign.START),
                            ]
                        ),                 
                    ]
                )
            )

        update_prof = ft.ElevatedButton(
        content=ft.Text("Atualizar Perfil", size=17, color=bgcolor, width=170, text_align=ft.TextAlign.CENTER),
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
            content=ft.Column(
                spacing=2,
                #alignment=ft.MainAxisAlignment.CENTER,
                controls=[ 
                    ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Text("Aluno UVV", size=22),
                            ft.Text("ID: 25030024", size=11)
                        ],spacing=-2
                    ),
                    ft.Column(
                        controls=[
                            ft.Text("Configurações de conta", size=18 ),
                            ft.Column(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                ft.Text("Nome De Usuário"),
                                ft.TextField(label="", border_radius=10, width=330, fill_color="white", content_padding=10, height=38, color="black"),
                                ], spacing=1
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("Telefone"),
                                ft.TextField(hint_text="00 0000-0000", border_radius=10, width=330, fill_color="white", content_padding=10, height=38, color="black"),                           
                                ], spacing=1
                            ),
                            ft.Column(
                                controls=[
                                ft.Text("E-mail"),
                                ft.TextField(label="", border_radius=10, width=330, fill_color="white", content_padding=10, height=38, color="black"),
                                ], spacing=1
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            update_prof
                        ]
                    )
                ],
            )
        )

        page.add(ft.Column(
            expand=True,
            auto_scroll=True,
            controls=[
                titulo,
                base
            ]
        ))

        return ft.View(route="/prof", expand=True, auto_scroll=True, controls=[titulo, base])

