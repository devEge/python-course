import tkinter as tk


class LabelHeight:
    def __init__(self, root):
        self._label_height = tk.Label(root, text="Enter your Height (cm)", font=("Arial", 12, "normal"))
        self._label_height.pack(padx=5, pady=5)
