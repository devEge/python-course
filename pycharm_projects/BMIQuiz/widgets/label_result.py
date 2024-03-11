import tkinter as tk


class LabelResult:
    def __init__(self, root):
        self._label_result = tk.Label(root, text="", font=("Helvetica", 15, "normal"))
        self._label_result.pack(side="bottom", pady=20)

    def set_result(self, text):
        self._label_result.config(text=text)
