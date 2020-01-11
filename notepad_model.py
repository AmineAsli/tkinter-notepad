class NotepadModel:

    def __init__(self):
        self.filename = None
    
    def new_file(self):
        self.filename = None
    
    def open_file(self, filename):
        self.filename = filename