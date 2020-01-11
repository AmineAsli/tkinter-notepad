from mediator import Mediator
from notepad_view import NotepadView

class NotepadController(Mediator):
    def __init__(self):
        self.view = NotepadView(self)
    
    def run(self):
        self.view.setup_window()
    
    def notify(self, sender, event):
        if event == 'new_file':
            print('new_file')