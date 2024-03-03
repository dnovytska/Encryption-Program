import tkinter as tk
from interface import Interface
from encryption import codification, decodification

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root, codification, decodification)
    app.create_widgets()
    root.mainloop()
