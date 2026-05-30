import tkinter as tk
from tkinter import ttk
from controllers.user_controller import get_users


def run_app():
    root = tk.Tk()
    root.title("Лабораторная работа")
    root.geometry("500x300")

    tree = ttk.Treeview(root, columns=("ID", "Name"), show="headings")

    tree.heading("ID", text="ID")
    tree.heading("Name", text="Имя")

    tree.pack(fill="both", expand=True)

    for user in get_users():
        tree.insert("", "end", values=user)

    root.mainloop()