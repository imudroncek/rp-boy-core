from core.Screen import Screen

class CountScreen(Screen):
    count = 0
    pause = False
    
    def callback():
        pass
    
    def count_up(self):
        self.count = self.count + 1
    
    def _render(self):
        if (not self.pause):
            self.display.text(str(self.count), 1, 1, 1)
            self.count_up()

    def _a_pressed(self):
        self.pause = not self.pause_menu
        
    def _b_pressed(self):
        pass

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
            
        
    