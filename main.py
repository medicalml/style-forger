import cv2
import numpy as np
import Tkinter as tk
from ApplicationCanvas import ApplicationCanvas

root = tk.Tk()
root.attributes("-fullscreen",True)
app = ApplicationCanvas(root)
root.mainloop()