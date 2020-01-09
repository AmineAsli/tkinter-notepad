from notepad_view import NotepadView

class NotepadController:
    def __init__(self):
        self.view = NotepadView()
        
    def run(self):
        self.view.setup_window()