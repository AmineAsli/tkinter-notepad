from colleague import Colleague

class NotepadModel(Colleague):

    def __init__(self):
        self.filename = None
        self.filecontent = None

    def new_file(self):
        self.filename = None
    
    def open_file(self, filename):
        self.filename = filename
        if self.filename:
            with open(self.filename) as file:
                self.filecontent = file.read()
                self.mediator.notify(self, 'file_content')