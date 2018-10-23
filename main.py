"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

from ttkthemes import themed_tk as ttk

from interface.pages import *


class Nexus(object):
    def __init__(self):
        notebook = Notebook()
        page_1 = Frame(notebook)
        page_2 = Frame(notebook)
        page_3 = Frame(notebook)
        page_4 = Frame(notebook)

        notebook.add(page_1, text="Base Sheet")
        notebook.add(page_2, text="Advanced Sheet")
        notebook.add(page_3, text="Creation Guidelines")
        notebook.add(page_4, text="Setting Information")

        sheet = CoreSheet(page_1, padding=10)
        sheet.grid(row=0, column=0, columnspan=2)

        notebook.pack()


root = ttk.ThemedTk()
root.title("Nexus - Sheet Builder")
root.resizable(False, False)
"""
List of available themes from root.get_themes()
['classic', 'ubuntu', 'keramik_alt', 'elegance', 'equilux', 'black', 'default', 'arc', 'radiance', 
'plastik', 'aquativo', 'keramik', 'clam', 'winxpblue', 'clearlooks', 'kroc', 'blue', 'alt']
"""
root.set_theme("ubuntu")

app = Nexus()

root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.mainloop()
