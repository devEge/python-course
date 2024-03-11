import tkinter as tk
from services.input_service import InputService


class EntryHeight:
    def __init__(self, root):
        self._entry_height = tk.Entry(root, font=("Arial", 12, "normal"), width=20, validate="key",
                                      validatecommand=(root.register(InputService.only_numbers), '%S'))
        self._entry_height.pack(padx=5, pady=5)

    def getData(self):
        return self._entry_height.get()
