import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "App Pets - Fluxo"
    page.theme_mode = "light"
    page.padding = 0
    page.spacing = 0

    # Estado simples do fluxo de cadastro
    state = {
        "pet_photo": None,
        "pet_name": "",
        "pet_gender": "",
        "pet_birth": None,
        "pet_breed": "",
        "remember_me": False,
        "email": "",
    }

    # ---------- Utilidades compartilhadas ----------
    def app_bar(title: str, can_back: bool = True):
        return ft.AppBar(
            title=ft.Text(title),
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda e: page.on_view_pop(page.views[-1]) if can_back and len(page.views) > 1 else None,
                disabled=not can_back or len(page.views) <= 1,
            ),
        )


    # ---------- VIEWS ----------
    def view_intro():
        return ft.View(
            route="/",
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.TEAL_700,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.CircleAvatar(
                                radius=50,
                                bgcolor=ft.Colors.TEAL_100,
                                content=ft.Icon(ft.Icons.PETS, size=50, color=ft.Colors.TEAL_900),
                            ),
                            ft.Container(height=20),
                            ft.FilledButton(
                                "Login",
                                icon=ft.Icons.LOGIN,
                                on_click=lambda e: page.go("/login"),
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                            ),
                        ],
                    ),
                )
            ],
        )

    def view_login():
        email = ft.TextField(label="E-mail ou telefone", value=state.get("email", ""), on_change=lambda e: state.__setitem__("email", e.control.value))
        senha = ft.TextField(label="Senha", password=True, can_reveal_password=True)
        lembrar = ft.Checkbox(label="Lembrar", value=state["remember_me"], on_change=lambda e: state.__setitem__("remember_me", e.control.value))

        return ft.View(
            route="/login",
            appbar=app_bar("Login", can_back=True),
            controls=[
                ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Column(
                        spacing=16,
                        controls=[
                            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                                ft.CircleAvatar(radius=36, bgcolor=ft.Colors.TEAL_100, content=ft.Icon(ft.Icons.PETS, color=ft.Colors.TEAL_900))
                            ]),
                            ft.Text("Login", size=22, weight=ft.FontWeight.BOLD),
                            email,
                            senha,
                            ft.Row([lembrar, ft.TextButton("Esqueci a senha")], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            ft.FilledButton("Entrar", icon=ft.Icons.LOGIN, on_click=lambda e: page.go("/cadastro/nome")),
                            ft.Divider(),
                            ft.Text("Ou entre com"),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                controls=[
                                    ft.OutlinedButton("Google"),
                                    ft.OutlinedButton("Apple"),
                                    ft.OutlinedButton("Facebook"),
                                ],
                            ),
                            ft.TextButton("Criar conta", on_click=lambda e: page.go("/cadastro/nome")),
                        ],
                    ),
                )
            ],
        )

    def view_cadastro_nome():
        # Campo de nome + imagem com botão de editar
        nome_tf = ft.TextField(
            label="Qual é o nome do seu cachorro?",
            hint_text="Ex.: Thor",
            value=state["pet_name"],
            on_change=lambda e: state.__setitem__("pet_name", e.control.value),
        )

        avatar = ft.Stack(
            [
                ft.CircleAvatar(
                    radius=60,
                    bgcolor=ft.Colors.GREY_200,
                    foreground_image_src=None,
                    content=ft.Icon(ft.Icons.PETS, size=48, color=ft.Colors.GREY_600),
                ),
                ft.Container(
                    content=ft.IconButton(icon=ft.Icons.CAMERA_ALT, on_click=lambda e: file_picker.pick_files(allow_multiple=False)),
                    right=0,
                    bottom=0,
                ),
            ],
            width=140,
            height=140,
        )

        return ft.View(
            route="/cadastro/nome",
            appbar=app_bar("Cadastro"),
            controls=[
                ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Column(
                        spacing=16,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Vamos lá?", size=22, weight=ft.FontWeight.BOLD),
                            avatar,
                            nome_tf,
                            ft.FilledButton("Avançar", on_click=lambda e: page.go("/cadastro/sexo")),
                        ],
                    ),
                )
            ],
        )

    def view_cadastro_sexo():
        rg = ft.RadioGroup(
            value=state["pet_gender"],
            on_change=lambda e: state.__setitem__("pet_gender", e.control.value),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Radio(value="Fêmea", label="Fêmea"),
                    ft.Radio(value="Macho", label="Macho"),
                ],
            ),
        )

        return ft.View(
            route="/cadastro/sexo",
            appbar=app_bar("Cadastro"),
            controls=[
                ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Column(
                        spacing=16,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Sexo do Pet", size=22, weight=ft.FontWeight.BOLD),
                            rg,
                            ft.FilledButton("Avançar", on_click=lambda e: page.go("/cadastro/idade")),
                        ],
                    ),
                )
            ],
        )

    def view_cadastro_idade():
        data_tf = ft.TextField(
            label="Qual a idade do seu cachorro? (data de nascimento)",
            read_only=True,
            value=state["pet_birth"].strftime("%d/%m/%Y") if state["pet_birth"] else "",
            suffix=ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, on_click=lambda e: open_datepicker(data_tf)),
        )

        return ft.View(
            route="/cadastro/idade",
            appbar=app_bar("Cadastro"),
            controls=[
                ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Column(
                        spacing=16,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Idade", size=22, weight=ft.FontWeight.BOLD),
                            data_tf,
                            ft.FilledButton("Avançar", on_click=lambda e: page.go("/cadastro/raca")),
                        ],
                    ),
                )
            ],
        )

    def view_cadastro_raca():
        breeds = [
            "Sem Raça Definida", "Labrador", "Poodle", "Bulldog",
            "Shih Tzu", "Pastor Alemão", "Golden Retriever", "Beagle", "Husky Siberiano",
        ]

        grid = ft.GridView(
            expand=True,
            runs_count=2,
            max_extent=220,
            child_aspect_ratio=1.2,
            spacing=10,
            run_spacing=10,
        )

        def make_tile(label: str):
            selected = label == state["pet_breed"]
            return ft.Container(
                on_click=lambda e, l=label: select_breed(l),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.PETS, size=48, color=ft.Colors.TEAL_700 if selected else ft.Colors.GREY_600),
                        ft.Text(label, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ],
                ),
                border=ft.border.all(2, ft.Colors.TEAL_700 if selected else ft.Colors.GREY_300),
                border_radius=10,
                padding=10,
            )

        def select_breed(label: str):
            state["pet_breed"] = label
            # Re-render tiles to refletir seleção
            grid.controls.clear()
            for b in breeds:
                grid.controls.append(make_tile(b))
            page.update()

        for b in breeds:
            grid.controls.append(make_tile(b))

        def concluir(_):
            page.snack_bar = ft.SnackBar(ft.Text("Cadastro concluído!"))
            page.snack_bar.open = True
            page.update()
            page.go("/login")

        return ft.View(
            route="/cadastro/raca",
            appbar=app_bar("Cadastro"),
            controls=[
                ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Column(
                        expand=True,
                        spacing=16,
                        controls=[
                            ft.Text("Raça", size=22, weight=ft.FontWeight.BOLD),
                            ft.Container(expand=True, content=grid),
                            ft.FilledButton("Concluir", on_click=concluir),
                        ],
                    ),
                )
            ],
        )

    # ---------- Navegação ----------
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(view_intro())
        elif page.route == "/login":
            page.views.append(view_login())
        elif page.route == "/cadastro/nome":
            page.views.append(view_cadastro_nome())
        elif page.route == "/cadastro/sexo":
            page.views.append(view_cadastro_sexo())
        elif page.route == "/cadastro/idade":
            page.views.append(view_cadastro_idade())
        elif page.route == "/cadastro/raca":
            page.views.append(view_cadastro_raca())
        else:
            page.views.append(view_intro())
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(main)
