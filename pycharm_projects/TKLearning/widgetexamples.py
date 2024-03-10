import tkinter as tk

root = tk.Tk()
root.title("Widget Examples")
root.minsize(width=800, height=600)

# Label
label = tk.Label(root, text="My Label")
label.config(bg="black", fg="white", padx=10, pady=10, font="Arial")
label.pack()


# Button Function
def button_clicked():
    print("Button clicked")


# Button
button = tk.Button(root, text="Button", command=button_clicked)
button.pack(pady=10)

# Multiline
text = tk.Text(width=50)
text.pack()

# Scale
scale = tk.Scale(root, from_=0, to=100)
scale.pack()

# Spinbox
spin = tk.Spinbox(root, from_=0, to=100)
spin.pack()

# Check Button Function
def check_button():
    print(check_state.get())


# Check Button
check_state = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Checkbutton", variable=check_state, command=check_button)
checkbutton.pack()


# Radio Button Function
def radio_selected():
    print(radio_checked_state.get())


# Radio Buttons
radio_checked_state = tk.IntVar()
radio_button = tk.Radiobutton(root, text="1. Option", value=10, variable=radio_checked_state, command=radio_selected)
radio_button_2 = tk.Radiobutton(root, text="1. Option", value=20, variable=radio_checked_state, command=radio_selected)
radio_button.pack()
radio_button_2.pack()


def list_box_selected(event):
    print(listbox.get(listbox.curselection()))


# Listbox
listbox = tk.Listbox(root)
name_list = ["<NAME>", "<NAME>", "<NAME>", "<NAME>"]
for i in range(len(name_list)):
    listbox.insert(i, name_list[i])
listbox.bind("<<ListboxSelect>>", list_box_selected)
listbox.pack()

root.mainloop()
