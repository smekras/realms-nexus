"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

from ttkthemes import themed_tk as tk

from interface.pages import *


class Nexus(object):
    def __init__(self):
        notebook = Notebook()
        f1 = BaseSheet(notebook)
        f2 = Frame(notebook)
        f3 = Frame(notebook)
        f4 = Frame(notebook)
        notebook.add(f1, text="Base Sheet")
        notebook.add(f2, text="Advanced Sheet")
        notebook.add(f3, text="Creation Guidelines")
        notebook.add(f4, text="Setting Information")

        notebook.pack()


root = tk.ThemedTk()
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
