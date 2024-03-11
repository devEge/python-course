import tkinter as tk


class LabelWeight:
    def __init__(self, root):
        self._label_weight = tk.Label(root, text="Enter your Weight (kg)", font=("Arial", 12, "normal"))
        self._label_weight.pack(padx=5, pady=5)
