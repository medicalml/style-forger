import tkinter as tk
from Application import Application
from Style import Style

transferedArtStyles = [
    Style("Starry night", "chainer_fast_neuralstyle/models/thumbnails/starry-night.jpg", "chainer_fast_neuralstyle/models/starry.model"),
    Style("Kanagawa", "chainer_fast_neuralstyle/models/thumbnails/kanagawa-style.jpg", "chainer_fast_neuralstyle/models/kanagawa.model"),
    Style("Kandinsky", "chainer_fast_neuralstyle/models/thumbnails/kandinsky.jpg", "chainer_fast_neuralstyle/models/kandinsky_e2_full512.model"),
    Style("Candy", "chainer_fast_neuralstyle/models/thumbnails/candy-style.jpg", "chainer_fast_neuralstyle/models/candy_512_2_49000.model"),
    Style("Cubist", "chainer_fast_neuralstyle/models/thumbnails/cubist-style.jpg", "chainer_fast_neuralstyle/models/cubist.model")
]

root = tk.Tk()
root.attributes("-fullscreen",True)

app = Application(root, transferedArtStyles)
root.mainloop()
