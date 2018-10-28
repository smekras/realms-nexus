"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

from ttkthemes import themed_tk as ttk

from interface.pages import *
from logic.entities import *
from logic.utils import *
from tools.roller import *


class Nexus(object):
    def __init__(self, master):
        self.master = master
        menu = Menu()
        self.master.config(menu=menu)
        self.source = read_json_file('data/template.json')
        self.character = Character(self.source)
        self.temp = {}
        self.sheet = None

        file = Menu(menu, tearoff=0)
        file.add_command(label="New", command=self.create_sheet)
        file.add_command(label="Load", command=self.load_sheet)
        file.add_command(label="Save", command=self.save_sheet)
        file.add_separator()
        file.add_command(label="Exit", command=self.client_exit)

        tools = Menu(menu, tearoff=0)
        tools.add_command(label="Dice Roller", command=self.dice_roller)
        tools.add_command(label="Image Gallery", command=self.client_exit)
        
        info = Menu(menu, tearoff=0)
        info.add_command(label="About", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)
        menu.add_cascade(label="Tools", menu=tools)
        menu.add_cascade(label="Help", menu=info)

        notebook = Notebook()
        self.page_1 = Frame(notebook)
        page_2 = Frame(notebook)
        page_3 = Frame(notebook)
        page_4 = Frame(notebook)

        notebook.add(self.page_1, text="Base Sheet")
        notebook.add(page_2, text="Advanced Sheet")
        notebook.add(page_3, text="Creation Guidelines")
        notebook.add(page_4, text="Setting Information")

        self.sheet = CoreSheet(self.page_1, self.character, padding=10)
        self.populate_sheet()

        notebook.pack()

    def create_sheet(self):
        self.source = read_json_file('data/template.json')

    def load_sheet(self):
        f = open(askopenfilename())
        if f is None:
            return
        else:
            self.source = read_json_file(f.name)
            self.sheet.pack_forget()
            self.populate_sheet()

    def save_sheet(self):
        self.temp = self.source
        f = asksaveasfilename(defaultextension=".json")
        if f is None:
            return
        else:
            create_json_file(f, self.temp)

    def populate_sheet(self):
        self.sheet = CoreSheet(self.page_1, self.character, padding=10)
        self.sheet.pack(fill=BOTH, expand=1)

    def dice_roller(self):
        anchor = Toplevel(self.master)
        roller_app = RollerApp(anchor)

    @staticmethod
    def client_exit():
        exit()


root = ttk.ThemedTk()
root.title("Nexus - Sheet Builder")
root.resizable(False, False)
"""
List of available themes from root.get_themes()
['classic', 'ubuntu', 'keramik_alt', 'elegance', 'equilux', 'black', 'default', 'arc', 'radiance', 
'plastik', 'aquativo', 'keramik', 'clam', 'winxpblue', 'clearlooks', 'kroc', 'blue', 'alt']
"""
root.set_theme("ubuntu")
icon = PhotoImage(file=r'images/nexus.png')
root.tk.call('wm', 'iconphoto', root._w, icon)

app = Nexus(root)

root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.mainloop()
