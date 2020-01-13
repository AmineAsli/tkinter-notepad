from tkinter import Tk, Text, Scrollbar, Menu, messagebox, END
from colleague import Colleague

class NotepadView(Colleague):
    APPLICATION_NAME = "Notepad"
    VERSION = '0.01'
    SCREEN_SIZE = '350x350'

    def __init__(self):
        self.root = Tk()
    
    def setup_window(self):
        self.root.geometry(self.SCREEN_SIZE)
        self.root.title(self.APPLICATION_NAME)
        self.setup_menu()
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

    # Getter function
    @property
    def filename(self):
        return self._filename

    # Setter function
    @filename.setter
    def filename(self, value):
        self._filename = value

    def select_all(self, event=None):
        self.document_area.tag_add('sel', '1.0', 'end')
        return 'break'
    
    def new(self, event=None):
        self.filename = None
        self.document_area.delete(1.0, END)
    
    def cut(self):
         self.document_area.event_generate('<<Cut>>')
    
    def copy(self):
        self.document_area.event_generate('<<Copy>>')

    def paste(self):
        self.document_area.event_generate('<<Paste>>')

    def undo(self):
        self.document_area.event_generate('<<Undo>>')

    def redo(self, event=None):
        self.document_area.event_generate('<<Redo>>')
        return 'break'
    
    def about(self):
        messagebox.showinfo("About", f"{self.APPLICATION_NAME} {self.VERSION}")
    
    def bind_keyboard_events(self):
        self.document_area.bind('<Control-A>', self.select_all)
        self.document_area.bind('<Control-a>', self.select_all)
        self.document_area.bind('<Control-Y>', self.redo)
        self.document_area.bind('<Control-y>', self.redo)
        self.document_area.bind('<Control-N>', self.new)
        self.document_area.bind('<Control-n>', self.new)

    def setup_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
       
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About Notepad", command=self.about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)