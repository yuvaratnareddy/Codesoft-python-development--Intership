import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        password_length = int(entry_length.get())
        if password_length <= 0:
            result_label.config(text="Please enter a valid password length.", fg="red")
        else:
            password = generate_password(password_length)
            result_label.config(text="Generated Password: " + password, fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid number for the password length.", fg="red")


window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")  


instruction_label = tk.Label(window, text="Enter the desired length of the password:", font=("Helvetica", 12))
instruction_label.pack(pady=10)

entry_length = tk.Entry(window, font=("Helvetica", 12))
entry_length.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password, font=("Helvetica", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)


window.mainloop()