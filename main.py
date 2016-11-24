import Tkinter as tk
from Application import Application

root = tk.Tk()
root.attributes("-fullscreen",True)

app = Application(root)
root.mainloop()
