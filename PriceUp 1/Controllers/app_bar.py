import flet as ft

def bottom_bar(page):
    
    return ft.BottomAppBar(
        bgcolor="#04043F",
        content=ft.Row(
            controls=[  # ✅ use controls no lugar de actions
                ft.IconButton(
                    icon=ft.Icons.HOME_OUTLINED,
                    tooltip="Home",
                    on_click=lambda _: page.go('/home')
                ),
                ft.IconButton(
                    icon=ft.Icons.ANALYTICS_OUTLINED,
                    tooltip="vetor",
                    # on_click=...
                ),
                ft.IconButton(
                    icon=ft.Icons.LAYERS_OUTLINED,
                    tooltip="sales",
                    on_click=lambda _: page.go('/product')
                ),
                ft.IconButton(
                    icon=ft.Icons.PERSON_OUTLINE,
                    tooltip="user",
                    on_click=lambda _: page.go('/profile')
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )
