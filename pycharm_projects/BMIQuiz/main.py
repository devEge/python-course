import tkinter as tk

# Widget Implementation
from widgets.entry_weight import EntryWeight
from widgets.label_weight import LabelWeight
from widgets.label_height import LabelHeight
from widgets.label_result import LabelResult
from widgets.entry_height import EntryHeight
from widgets.button_calculate import ButtonCalculate

# Main (root) Window
root = tk.Tk()

# Root Configs
root.title("BMI Calculator")
root.minsize(width=500, height=500)

# Weight Label Widget
label_weight = LabelWeight(root)
# Weight Entry Widget
entry_weight = EntryWeight(root)
# Height Label Widget
label_height = LabelHeight(root)
# Height Entry Widget
entry_height = EntryHeight(root)
# Result Label
label_result = LabelResult(root)
# Calculate Button
ButtonCalculate(root, entry_weight, entry_height, label_result)

root.mainloop()
