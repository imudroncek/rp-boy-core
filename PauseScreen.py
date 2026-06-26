from core.Screen import Screen
from core.Menu import Menu, MenuItem

class PauseScreen(Screen):

    def __init__(self,
                 width,
                 height,
                 display,
                 button_input,
                 screens_helper,
                 name = "Parent Screen Class",
                 parent = None,
                 active = False):
        super().__init__(width, height, display, button_input, screens_helper, name, parent, active)
        self.exit_item = MenuItem("Exit", screen_instance=self.parent)
        self.pause_menu = Menu([MenuItem("Resume"), self.exit_item])
    
    def callback():
        pass

    def set_paused_instance(self, instance):
        self.pause_menu = Menu([MenuItem("Resume", screen_instance=instance), self.exit_item])
    
    def _render(self):
        self._get_previous()
        self._get_selected()
        self._get_next()

    def _clear_dynamic_content(self):
        self.display.fill_rect(3, 43, self.width - 6, self.height - 86, 0)

    def _render_static_content(self):
        self.display.fill(1)
        self.display.fill_rect(3, 3, self.width - 6, self.height - 6, 0)
        self.display.text(self.name, 5, 5, 1)
        self.display.line(3, 14, self.width - 4, 14, 1)

    def _get_previous(self):
        if (self.pause_menu.has_previous_item()):
            self.display.text(self.pause_menu.get_item_shortname(self.pause_menu.get_selected_item_index()-1), 8, 49, 1)
            self.display.line(62, 45, 64, 43, 1)
            self.display.line(64, 43, 66, 45, 1)
            
    def _get_selected(self):
        self.display.rect(6, 57, self.width-12, 12, 1)
        self.display.line(7, 67, self.width-8, 67, 1)
        self.display.text(self.pause_menu.get_item_shortname(self.pause_menu.get_selected_item_index()), 8, 59, 1)

    def _get_next(self):
        if (self.pause_menu.has_next_item()):
            self.display.text(self.pause_menu.get_item_shortname(self.pause_menu.get_selected_item_index()+1), 8, 70, 1)
            self.display.line(62, 80, 64, 82, 1)
            self.display.line(64, 82, 66, 80, 1)

    def _a_pressed(self):
        if (self.pause_menu.has_previous_item()):
            self.pause_menu.previous_item()
            
    def _b_pressed(self):
        if (self.pause_menu.has_next_item()):
            self.pause_menu.next_item()

    def _start_pressed(self):
        self.deactivate()
        self.screens_helper.set_active_screen(self.pause_menu.get_selected_item().get_screen_instance())
        self.screens_helper.get_active_screen().init()
        self.screens_helper.get_active_screen().activate()
        self.pause_menu.reset()

    def _select_pressed(self):
        pass

    def _up_pressed(self):
        pass

    def _down_pressed(self):
        pass

    def _left_pressed(self):
        pass

    def _right_pressed(self):
        pass

    def _zl_pressed(self):
        pass

    def _zr_pressed(self):
        pass
            
