import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    label_password.config(text=f"Пароль: {password}")

root = tk.Tk()
root.title("Генератор паролей")

entry_length = tk.Entry(root, width=10)
entry_length.pack()

button_generate = tk.Button(root, text="Сгенерировать", command=generate_password)
button_generate.pack()

label_password = tk.Label(root, text="Пароль: ")
label_password.pack()

root.mainloop()
