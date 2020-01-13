import os
from tkinter import Tk, Text, Scrollbar, Menu, messagebox, filedialog, END
from colleague import Colleague

class NotepadView(Colleague):
    APPLICATION_NAME = "Notepad"
    VERSION = '0.01'
    SCREEN_SIZE = '350x350'

    def __init__(self):
        self.root = Tk()
        self.content = None
    
    def setup_window(self):
        self.root.geometry(self.SCREEN_SIZE)
        self.change_title(f"Untitled - {self.APPLICATION_NAME}")
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
    def content(self):
        return self._content

    # Setter function
    @content.setter
    def content(self, value):
        self._content = value

    def change_title(self, title):
        self.root.title(title)
        
    def select_all(self, event=None):
        self.document_area.tag_add('sel', '1.0', 'end')
        return 'break'
    
    def new(self, event=None):
        self.filename = None
        self.change_title(f"Untitled - {self.APPLICATION_NAME}")
        self.document_area.delete(1.0, END)
    
    def open(self, event=None):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", 
            filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if self.filename:
            self.change_title(f"{os.path.basename(self.filename)} - {self.APPLICATION_NAME}")
            self.document_area.delete(1.0, END)
            self.mediator.notify(self, 'open_file')
            if self.content:
                self.document_area.insert(1.0, self.content) 
    
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
        self.document_area.bind('<Control-O>', self.open)
        self.document_area.bind('<Control-o>', self.open)

    def setup_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new)
        file_menu.add_command(label="Open...", command=self.open)
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