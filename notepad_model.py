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
            try:
                with open(self.filename) as file:
                    self.filecontent = file.read()
                    self.mediator.notify(self, 'file_content')
            except Exception:
                self.mediator.notify(self, 'error_file')

    def save_file(self, filename, content):
        self.filename = filename
        self.filecontent = content

        try:
            with open(self.filename, 'w') as file:
                file.write(self.filecontent)
                self.mediator.notify(self, 'written_file')
        except Exception:
            self.mediator.notify(self, 'error_file_write')
