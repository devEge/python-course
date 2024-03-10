import tkinter as tk

window = tk.Tk()

# Window Configs
window.title("Python Tkinter Example")
window.minsize(width=800, height=600)

# Label
my_label = tk.Label(window, text="Hello World!")
my_label.config(bg="black", fg="white", font=('Arial', 30, 'bold'))
my_label.grid(row=0, column=0)


# Button Function
def click_button():
    print(my_entry.get())


# Button
my_button = tk.Button(window, text="This is a button", command=click_button)
my_button.grid(row=1, column=1)

# Entry
my_entry = tk.Entry(window, width=20)
my_entry.grid(row=2, column=2)

window.mainloop()
