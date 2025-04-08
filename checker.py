import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    suggestions = []

    length_ok = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_symbol = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    score = sum([bool(length_ok), bool(has_upper), bool(has_lower), bool(has_digit), bool(has_symbol)])

    if score == 5:
        strength = "Strong 💪"
    elif 3 <= score < 5:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    if not length_ok:
        suggestions.append("Use at least 8 characters.")
    if not has_upper:
        suggestions.append("Add uppercase letters.")
    if not has_lower:
        suggestions.append("Add lowercase letters.")
    if not has_digit:
        suggestions.append("Include numbers.")
    if not has_symbol:
        suggestions.append("Include special characters (e.g. !@#$%).")

    return strength, suggestions

def on_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, suggestions = check_password_strength(password)
    strength_label.config(text=f"Strength: {strength}")

    suggestion_text = "\n".join(suggestions) if suggestions else "Your password is secure!"
    suggestion_label.config(text=suggestion_text)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

# UI Elements
title = tk.Label(root, text="🔐 Password Strength Checker", font=("Helvetica", 14, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, show='*', width=30, font=("Helvetica", 12))
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check Strength", command=on_check, font=("Helvetica", 11))
check_btn.pack(pady=5)

strength_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
strength_label.pack(pady=5)

suggestion_label = tk.Label(root, text="", font=("Helvetica", 10), wraplength=380, justify="left")
suggestion_label.pack(pady=10)

root.mainloop()
