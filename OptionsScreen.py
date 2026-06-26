from core.Screen import Screen

class OptionsScreen(Screen):

    def __init__(self,
                 width,
                 height,
                 display,
                 canvas,
                 button_input,
                 screens_helper,
                 options,
                 name = "Parent Screen Class",
                 parent = None,
                 active = False):
        super().__init__(width, height, display, canvas, button_input, screens_helper, name, parent, active)
        self.options = options

    def _render(self):
        self._get_previous()
        self._get_selected()
        self._get_next()

    def _clear_dynamic_content(self):
        self.canvas.fill_rect(0, 43, self.width - 1, self.height - 86, 0)

    def _render_static_content(self):
        self._get_header()
        self._get_footer()

    def _get_header(self):
        self.canvas.text(self.name, 0, 0, 1)
        self.canvas.line(0, 8, self.width, 8, 1)

    def _get_footer(self):
        self.canvas.line(0, self.height-9, self.width, self.height-9, 1)
        self.canvas.text("Use Start", 0, self.height-7, 1)

    def _get_previous(self):
        if (self.options.options_menu.has_previous_item()):
            self.canvas.text(self.options.options_menu.get_item_shortname(self.options.options_menu.get_selected_item_index()-1), 5, 49, 1)
            self.canvas.line(62, 45, 64, 43, 1)
            self.canvas.line(64, 43, 66, 45, 1)
            
    def _get_selected(self):
        self.canvas.rect(3, 57, self.width-6, 12, 1)
        self.canvas.line(4, 67, self.width-5, 67, 1)
        self.canvas.text(self.options.options_menu.get_item_shortname(self.options.options_menu.get_selected_item_index()), 5, 59, 1)

    def _get_next(self):
        if (self.options.options_menu.has_next_item()):
            self.canvas.text(self.options.options_menu.get_item_shortname(self.options.options_menu.get_selected_item_index()+1), 5, 70, 1)
            self.canvas.line(62, 80, 64, 82, 1)
            self.canvas.line(64, 82, 66, 80, 1)
            
    
    def _a_pressed(self):
        self.last_button_pressed = 'A'
        if (self.options.options_menu.has_previous_item()):
            self.options.options_menu.previous_item()
            
    def _b_pressed(self):
        self.last_button_pressed = 'B'
        if (self.options.options_menu.has_next_item()):
            self.options.options_menu.next_item()
            
    def _start_pressed(self):
        selected_item = self.options.options_menu.get_selected_item()
        selected_item.handler()
        if (selected_item.closable):
            self.deactivate()
            self.screens_helper.set_active_screen(self.parent)
            self.screens_helper.get_active_screen().init()
            self.screens_helper.get_active_screen().activate()

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
