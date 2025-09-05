import flet as ft
import json
from typing import Optional, Dict, Any, List, cast

class AppController:

    def __init__(self, page: ft.Page):
        self.page = page
        self.current_view = "auth"
        self.active_phase_id: Optional[int] = None
        self.auth_controller = None

    def get_current_view(self) -> ft.Control:
            if self.current_view == "home":
                from home import homeView
                #return RoadmapView(self).build
            