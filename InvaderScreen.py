import framebuf
from Screen import Screen

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
    
    def callback():
        pass
    
    def _render(self):
        if (self.counter >= 0 and self.counter <= 119):
            if (self.counter == 0 or self.counter == 119):
                self.flip = not self.flip
            if (self.flip):
                self.counter -= 1
            else:
                self.counter += 1
        self.display.blit(self.canvas, self.counter, 0)
            
        
    