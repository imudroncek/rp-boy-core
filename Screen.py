from abc import ABC, abstractmethod

class Screen(ABC):
    
    def __init__(self,
                 width,
                 height,
                 display,
                 canvas,
                 button_input,
                 screens_helper,
                 name = "Parent Screen Class",
                 parent = None,
                 active = False):
        self.parent = parent
        self.button_input = button_input
        self.screens_helper = screens_helper
        self.name = name
        self.width = width
        self.height = height
        self.display = display
        self.canvas = canvas
        self.active = active

    def render(self):
        if self.active:
            self._clear_dynamic_content()
            self._render()
            self.display.blit(self.canvas, 0, 0)
        self.display.show()

    @abstractmethod
    def _clear_dynamic_content(self):
        pass

    @abstractmethod
    def _render_static_content(self):
        pass
        
    @abstractmethod
    def _render(self):
        pass

    def _button_pressed(self, button_method):
        if self.active:
            button_method()
      
    def _a(self):
        self._button_pressed(self._a_pressed)
      
    @abstractmethod
    def _a_pressed(self):
        pass
      
    def _b(self):
        self._button_pressed(self._b_pressed)
      
    @abstractmethod
    def _b_pressed(self):
        pass
      
    def _start(self):
        self._button_pressed(self._start_pressed)
      
    def _start_pressed(self):
        self.deactivate()
        self.screens_helper.show_pause_screen()
      
    def _select(self):
        self._button_pressed(self._select_pressed)
      
    @abstractmethod
    def _select_pressed(self):
        pass
      
    def _up(self):
        self._button_pressed(self._up_pressed)
      
    @abstractmethod
    def _up_pressed(self):
        pass
      
    def _down(self):
        self._button_pressed(self._down_pressed)
      
    @abstractmethod
    def _down_pressed(self):
        pass
      
    def _left(self):
        self._button_pressed(self._left_pressed)
      
    @abstractmethod
    def _left_pressed(self):
        pass
      
    def _right(self):
        self._button_pressed(self._right_pressed)
      
    @abstractmethod
    def _right_pressed(self):
        pass
      
    def _zl(self):
        self._button_pressed(self._zl_pressed)
      
    @abstractmethod
    def _zl_pressed(self):
        pass
      
    def _zr(self):
        self._button_pressed(self._zr_pressed)
      
    @abstractmethod
    def _zr_pressed(self):
        pass
        
    def init(self):
        self.button_input.a.physical_button.when_pressed=self._a
        self.button_input.b.physical_button.when_pressed=self._b
        self.button_input.start.physical_button.when_pressed=self._start
        self.button_input.select.physical_button.when_pressed=self._select
        self.button_input.up.physical_button.when_pressed=self._up
        self.button_input.down.physical_button.when_pressed=self._down
        self.button_input.left.physical_button.when_pressed=self._left
        self.button_input.right.physical_button.when_pressed=self._right
        self.button_input.zl.physical_button.when_pressed=self._zl
        self.button_input.zr.physical_button.when_pressed=self._zr
        self.canvas.fill(0)
        self._render_static_content()
        self.display.blit(self.canvas, 0, 0)
        self.display.show()
        
    def activate(self):
        self.active = True
        
    def deactivate(self):
        self.active = False
