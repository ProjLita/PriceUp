# app/main.py
import flet as ft
from pages.splash_screen import splash_view as splash_view
from pages.login import login as login_view
from pages.login2 import login2 as login2_view
from pages.login3 import login3 as login3_view
from pages.home import homeView as home_view
from pages.sales import SalesView as sales_view
from pages.prof import Profile as profile_view
from pages.products import ProdView as prod_view
from pages.edit_sale import Edit_Sales as edit_view
from pages.add_prod import Add_Sales as add_view
from Controllers.app_bar import bottom_bar  # sua BottomAppBar

def main(page: ft.Page):
    page.title = "PriceUp - Fluxo"
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO

    def route_change(route):
        page.views.clear()

        # Rotas que terão a BottomAppBar
        rotas_com_bottom_bar = ["/home", "/profile", "/sales", "/product"]

        # Adiciona a AppBar apenas se a rota estiver na lista
        if page.route in rotas_com_bottom_bar:
            page.bottom_appbar = bottom_bar(page)  # ✅ CORRETO
        else:
            page.bottom_appbar = None

        # Adiciona a view conforme a rota
        r = page.route
        if r == "/":
            page.views.append(splash_view(page))
        elif r == "/login":
            page.views.append(login_view(page))
        elif r == "/login2":
            page.views.append(login2_view(page))
        elif r == "/login3":
            page.views.append(login3_view(page))        
        elif r == "/home":
            page.views.append(home_view(page))
        elif r == "/profile":
            page.views.append(profile_view(page))    
        elif r == "/sales":
            page.views.append(sales_view(page))
        elif r == "/product":
            page.views.append(prod_view(page))
        elif r == "/edit_sale":
            page.views.append(edit_view(page))
        elif r == "/add_prod":
            page.views.append(add_view(page))    
        else:
            pass

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)