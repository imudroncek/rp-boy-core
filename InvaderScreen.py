import framebuf
from core.Screen import Screen

class InvaderScreen(Screen):
    counter = 1
    flip = False
    invader = bytearray([
        0b10000001,  # █      █
        0b00100100,  #   █  █  
        0b01111110,  #  ██████ 
        0b11011011,  # ██ ██ ██
        0b11111111,  # ████████
        0b00111100,  #   ████  
        0b01000010,  #  █    █ 
        0b10100101   # █ █  █ █
    ])
    canvas = framebuf.FrameBuffer(invader, 8, 8, framebuf.MONO_HMSB)
    
    def _render(self):
        if (self.counter >= 0 and self.counter <= 119):
            if (self.counter == 0 or self.counter == 119):
                self.flip = not self.flip
            if (self.flip):
                self.counter -= 1
            else:
                self.counter += 1
        self.display.blit(self.canvas, self.counter, 0)

    def _clear_dynamic_content(self):
        self.display.fill_rect(0, 0, self.width - 1, 9, 0)

    def _render_static_content(self):
        pass

    def _a_pressed(self):
        pass

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
            
        
    