import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title('Генератор паролей')

        self.length_label = tk.Label(root, text="Длина пароля:")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        self.unclude_uppercase = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(root, text ="Включить заглавные буквы",
            variable=self.include_uppercase)
        self.uppercase_check.pack(pady=5)

        self.include_numbers = tk.BooleanVar()
        self.numbers.check = tk.Checkbutton(root, text="Включить цифры",
            variable=self.include_numbers)
        self.numbers_check.pack(pady=5)
        
        self.include_special = tk.BooleanVar()
        self.special_check = tk.Checkbutton(root, text="Включить специальные символы",
            variable=self.include_special)
        self.special_check.pack(pady=5)

        self.generate_button = tk.BooleanVar(root, text="Сгенерировать пароль", 
            command=self.generate_password)
        self.generate_button.pack(pady=20)

        self.password_entry = tk.Entry(root, width=30)
        self.password_entry.pack(pady=5)

    def generate_password(self):
        length = self.length_entry.get()

        if not length.isdigit():
            messagebox.showerror("Ошибка", "Введите корректную длину пароля.")
            return
        
        length = int(length)
        if length <= 0:
            messagebox.showerror("Ошибка", "Длина пароля должна быть больше 0.")
            return
        
        characters = string.ascii_lowercase
        if self.include_uppecase.get():
            characters += string.ascii_uppercase
        if self.include_numbers.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Ошибка", "Выберите хотя бы один тип символов.")
            return
        
        password = ''.join(random.choice(characters) for _ in range (length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
