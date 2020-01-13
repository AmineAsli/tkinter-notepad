from mediator import Mediator
from notepad_view import NotepadView
from notepad_model import NotepadModel

class NotepadController(Mediator):
    def __init__(self):
        self.view = NotepadView()
        self.view.mediator = self
        self.model = NotepadModel()
        self.model.mediator = self
    
    def run(self):
        self.view.setup_window()
    
    def notify(self, sender, event):
        if event == 'open_file':
            self.model.open_file(sender.filename)
        elif event == 'file_content':
            self.view.content = sender.filecontent