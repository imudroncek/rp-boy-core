from Screen import Screen
from Menu import Menu, MenuItem
from ButtonInput import ButtonInput
from ssd1306 import SSD1306_I2C
from ScreensHelper import ScreensHelper
from MainScreen import MainScreen

class PauseScreen(Screen):

    def __init__(self,
                 width: int,
                 height: int,
                 display: SSD1306_I2C,
                 button_input: ButtonInput,
                 screens_helper: ScreensHelper,
                 name: str = "Parent Screen Class",
                 parent: Screen = None,
                 active: bool = False):
        super().__init__(width, height, display, button_input, screens_helper, name, parent, active)
        self.exit_item = MenuItem("Exit", screen_instance=self.parent)
        self.pause_menu = Menu([MenuItem("Resume"), self.exit_item])
    
    def callback():
        pass

    def set_paused_instance(self, instance):
        self.pause_menu = Menu([MenuItem("Resume", screen_instance=instance), self.exit_item])
    
    def _render(self):
        self._get_header()
        self._get_previous()
        self._get_selected()
        self._get_next()

    def _get_header(self):
        self.display.fill(1)
        self.display.fill_rect(3, 3, self.width - 6, self.height - 6, 0)
        self.display.text(self.name, 5, 5, 1)
        self.display.line(3, 14, self.width - 6, 14, 1)

    def _get_previous(self):
        if (self.pause_menu.has_previous_item()):
            self.display.text(self.pause_menu.get_item_shortname(self.pause_menu.get_selected_item_index()-1), 8, 21, 1)
            self.display.line(62, 17, 64, 15, 1)
            self.display.line(64, 15, 66, 17, 1)
            

    def _get_selected(self):
        self.display.rect(6, 29, self.width-9, 12, 1)
        self.display.line(7, 39, self.width-8, 39, 1)
        self.display.text(self.pause_menu.get_item_shortname(self.pause_menu.get_selected_item_index()), 8, 31, 1)

    def _get_next(self):
        if (self.pause_menu.has_next_item()):
            self.display.text(self.pause_menu.get_item_shortname(self.pause_menu.get_selected_item_index()+1), 8, 42, 1)
            self.display.line(62, 52, 64, 54, 1)
            self.display.line(64, 54, 66, 52, 1)

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
            
