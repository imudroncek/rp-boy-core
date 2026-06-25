from core.Screen import Screen

class MainScreen(Screen):

    def __init__(self,
                 width,
                 height,
                 display,
                 button_input,
                 screens_helper,
                 main_menu,
                 name = "Parent Screen Class",
                 parent = None,
                 active = False):
        super().__init__(width, height, display, button_input, screens_helper, name, parent, active)
        self.last_button_pressed = None
        self.main_menu = main_menu

    def _render(self):
        self._get_header()
        self._get_previous()
        self._get_selected()
        self._get_next()
        self._get_footer()

    def _get_header(self):
        self.display.text(self.name, 0, 0, 1)
        self.display.line(0, 8, self.width, 8, 1)

    def _get_footer(self):
        self.display.line(0, self.height-9, self.width, self.height-9, 1)
        if (self.last_button_pressed != None):
            self.display.text(self.last_button_pressed, 0, self.height-7, 1)

    def _get_previous(self):
        if (self.main_menu.has_previous_item()):
            self.display.text(self.main_menu.get_item_shortname(self.main_menu.get_selected_item_index()-1), 5, 49, 1)
            self.display.line(62, 45, 64, 43, 1)
            self.display.line(64, 43, 66, 45, 1)
            
    def _get_selected(self):
        self.display.rect(3, 57, self.width-6, 12, 1)
        self.display.line(4, 67, self.width-5, 67, 1)
        self.display.text(self.main_menu.get_item_shortname(self.main_menu.get_selected_item_index()), 5, 59, 1)

    def _get_next(self):
        if (self.main_menu.has_next_item()):
            self.display.text(self.main_menu.get_item_shortname(self.main_menu.get_selected_item_index()+1), 5, 70, 1)
            self.display.line(62, 80, 64, 82, 1)
            self.display.line(64, 82, 66, 80, 1)
            
    
    def _a_pressed(self):
        self.last_button_pressed = 'A'
        if (self.main_menu.has_previous_item()):
            self.main_menu.previous_item()
            
    def _b_pressed(self):
        self.last_button_pressed = 'B'
        if (self.main_menu.has_next_item()):
            self.main_menu.next_item()

    def _start_pressed(self):
        self.last_button_pressed = 'Start'
        self.deactivate()
        self.screens_helper.set_active_screen(
            self.main_menu.get_selected_item().get_new_screen_instance(self.width, self.height, self.display, self.button_input, self.screens_helper, self)
        )
        self.screens_helper.get_active_screen().init()
        self.screens_helper.get_active_screen().activate()
            
    def _select_pressed(self):
        self.last_button_pressed = 'Select'

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
