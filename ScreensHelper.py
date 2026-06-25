class ScreensHelper:
    
    def __init__(self, active_screen = None, screens = []):
        self.active_screen = active_screen
        self.screens = screens
        self.pause_screen = None

    def set_pause_screen(self, pause_screen):
        self.pause_screen = pause_screen

    def show_pause_screen(self):
        self.active_screen = self.pause_screen
        self.get_active_screen().init()
        self.get_active_screen().activate()
        
    def get_active_screen(self):
        return self.active_screen
    
    def set_active_screen(self, screen):
        self.active_screen = screen
        self.pause_screen.set_paused_instance(self.active_screen)
        
    def get_screens(self):
        return self.screens
    
    def set_screens(self, screens):
        self.screens = screens