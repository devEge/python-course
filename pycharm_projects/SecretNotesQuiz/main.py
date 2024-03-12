import tkinter as tk
import tkinter.messagebox as msgbox
from services.encryption_service import EncryptionService

root = tk.Tk()


def encrypt_message():
    if len(input_text.get("1.0", tk.END)) == 0 or len(master_secret_input.get()) == 0:
        msgbox.showinfo(title="Error!", message="Please make sure of encrypted info.")
        return
    try:
        encrypted_message = EncryptionService.save_and_encrypt_notes(secret_data=input_text.get("1.0", tk.END),
                                                                     master_key=master_secret_input.get())
        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f'\n---{title_entry.get()}---\n{encrypted_message}')
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f'---{title_entry.get()}---\n{encrypted_message}')
        finally:
            title_entry.delete(0, tk.END)
            master_secret_input.delete(0, tk.END)
            input_text.delete("1.0", tk.END)
    except:
        msgbox.showinfo(title="Error!", message="Please make sure of encrypted info.")


def decrypt_message():
    try:
        decrypted_message = EncryptionService.decrypt_notes(input_text.get("1.0", tk.END), master_secret_input.get())
        title_entry.delete(0, tk.END)
        master_secret_input.delete(0, tk.END)
        input_text.delete('1.0', tk.END)
        input_text.insert("1.0", decrypted_message)
    except:
        msgbox.showinfo(title="Error!", message="Please make sure of encrypted info.")



root.title("SecretNotesQuiz")
root.minsize(width=400, height=600)
root.config(padx=30, pady=30)

logo = tk.PhotoImage(file="assets/top_secret_logo.png")
logo_label = tk.Label(root, image=logo)
logo_label.pack(pady=2)

title_info_label = tk.Label(text="Enter your title", font=("Verdena", 12, "normal"))
title_info_label.pack(pady=2)

title_entry = tk.Entry(width=30)
title_entry.pack(pady=2)

input_info_label = tk.Label(text="Enter your secret", font=("Verdena", 12, "normal"))
input_info_label.pack(pady=2)

input_text = tk.Text(width=50, height=25)
input_text.pack(pady=2)

master_secret_label = tk.Label(text="Enter master key", font=("Verdena", 12, "normal"))
master_secret_label.pack(pady=2)

master_secret_input = tk.Entry(width=30)
master_secret_input.pack(pady=2)

save_button = tk.Button(text="Save & Encrypt", command=lambda: encrypt_message())
save_button.pack(pady=2)

decrypt_button = tk.Button(text="Decrypt", command=lambda: decrypt_message())
decrypt_button.pack(pady=2)

root.mainloop()
