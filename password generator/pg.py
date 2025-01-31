import random
import string
import tkinter as tk
from tkinter import messagebox, ttk

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_special = special_var.get()
        
        chars = string.ascii_letters
        if use_digits:
            chars += string.digits
        if use_special:
            chars += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        check_password_strength(password)  # Check strength after generating password

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")

# Function to check password strength
def check_password_strength(password):
    if len(password) < 6:
        strength_label.config(text="Weak", fg="red")
    elif len(password) < 10:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Function to save password to a file
def save_password():
    password = password_entry.get()
    if password:
        with open("saved_passwords.txt", "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Success", "Password saved to file!")
    else:
        messagebox.showwarning("Warning", "No password to save!")

# Function to toggle dark mode
def toggle_dark_mode():
    if dark_mode_var.get():
        root.configure(bg="#333")
        for widget in root.winfo_children():
            widget.configure(bg="#333", fg="white")
    else:
        root.configure(bg="#f0f0f0")
        for widget in root.winfo_children():
            widget.configure(bg="#f0f0f0", fg="black")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Widgets
tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()
dark_mode_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", font=("Arial", 12), bg="#f0f0f0", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Special Characters", font=("Arial", 12), bg="#f0f0f0", variable=special_var).pack()
tk.Checkbutton(root, text="Dark Mode", font=("Arial", 12), bg="#f0f0f0", variable=dark_mode_var, command=toggle_dark_mode).pack()

tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4caf50", fg="white", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 14), justify="center", width=25)
password_entry.pack(pady=5)

strength_label = tk.Label(root, text="Strength: N/A", font=("Arial", 12), bg="#f0f0f0")
strength_label.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#008CBA", fg="white", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Save Password", font=("Arial", 12), bg="#ff9800", fg="white", command=save_password).pack(pady=5)

# Run the application
root.mainloop()
