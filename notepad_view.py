from tkinter import Tk, Text, Scrollbar

class NotepadView:
    APPLICATION_NAME = "Notepad"
    SCREEN_SIZE = '350x350'

    def __init__(self):
        self.root = Tk()
        
    def setup_window(self):
        self.root.geometry(self.SCREEN_SIZE)
        self.root.title(self.APPLICATION_NAME)
        self.setup_document_area()
        self.root.mainloop()

    def setup_document_area(self):
        self.document_area = Text(self.root, wrap='word', undo=1)
        self.document_area.pack(expand='yes', fill='both')

        x_scroll_bar = Scrollbar(self.document_area, orient='horizontal')
        y_scroll_bar = Scrollbar(self.document_area)
        self.document_area.configure(yscrollcommand=y_scroll_bar.set, xscrollcommand=x_scroll_bar.set)
        x_scroll_bar.config(command=self.document_area.xview)
        x_scroll_bar.pack(side='bottom', fill='x')
        y_scroll_bar.config(command=self.document_area.yview)
        y_scroll_bar.pack(side='right', fill='y')
        
        self.bind_keyboard_events()

    def select_all(self, event=None):
        self.document_area.tag_add('sel', '1.0', 'end')
        return 'break'

    def redo(self, event=None):
        self.document_area.event_generate('<<Redo>>')
        return 'break'
    
    def bind_keyboard_events(self):
        self.document_area.bind('<Control-A>', self.select_all)
        self.document_area.bind('<Control-a>', self.select_all)
        self.document_area.bind('<Control-Y>', self.redo)
        self.document_area.bind('<Control-y>', self.redo)
