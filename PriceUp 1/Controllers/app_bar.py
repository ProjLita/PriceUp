import flet as ft

class AppBar():

    def navBar (page):
        page.scroll = ft.ScrollMode.AUTO
        # Função para alternar tema claro/escuro
        def toggle_dark_mode(e):
            if page.theme_mode == "dark":
                page.theme_mode = "light"
            else:
                page.theme_mode = "dark"
            page.update()

        NavBar = ft.BottomAppBar(
            bgcolor="#04043F",
            content=ft.Row(
            actions=[
                ft.IconButton(
                    icon=ft.Icons.HOME_OUTLINED,
                    tooltip="Home",
                    #on_click=lambda _: page.go('/')
                ),
                ft.IconButton(
                    icon=ft.Icons.ANALYTICS_OUTLINED,
                    tooltip="vetor",
                   #on_click=toggle_dark_mode
                ),
                ft.IconButton(
                    icon=ft.Icons.LAYERS_OUTLINED,
                    tooltip="sales",
                    #on_click=lambda _: page.go('/settings')
                ),
                ft.IconButton(
                    icon=ft.Icons.PERSON_OUTLINE,
                    tooltip="user",
                   #on_click=toggle_dark_mode
                ),
            ]
        )
        )

        return NavBar
    

    # ft.IconButton(
    #                 icon=ft.Icons.HELP_OUTLINE,
    #                 tooltip="Ajuda",
    #                #on_click=toggle_dark_mode
    # )