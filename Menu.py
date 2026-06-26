class Menu:

    def __init__(self, items = []):
        self.items = items
        self.selected_item = 0

    def reset(self):
        self.selected_item = 0

    def add_item(self, item):
        self.items.append(item)

    def get_item_shortname(self, index):
        return self.items[index].shortname

    def has_next_item(self):
        return (self.selected_item >= 0 and self.selected_item < len(self.items)-1)

    def has_previous_item(self):
        return (self.selected_item > 0 and self.selected_item <= len(self.items)-1)
    
    def next_item(self):
        if (self.selected_item < len(self.items)-1):
            self.selected_item += 1

    def previous_item(self):
        if (self.selected_item > 0):
            self.selected_item -= 1

    def get_selected_item_index(self):
        return self.selected_item

    def get_selected_item(self):
        return self.items[self.selected_item]

class MenuItem:

    def __init__(self, name, screen_class=None, screen_instance=None):
        self.name = name
        self.shortname = self._shorten(self.name)
        self.screen_class = screen_class
        self.screen_instance = screen_instance

    def _shorten(self, text):
        if (len(text) > 15):
            return text[:12] + "..."
        return text

    def get_screen_instance(self):
        return self.screen_instance

    def get_new_screen_instance(self, width, height, display, canvas, button_input, screens_helper, parent):
        return self.screen_class(width, height, display, canvas, button_input, screens_helper, self.name, parent)
