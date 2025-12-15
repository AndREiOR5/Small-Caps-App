import tkinter as tk
from tkinter import ttk
import string

root = tk.Tk()
root.title("Small Caps Generator")
root.geometry("450x350")
root.configure(bg="#2c3e50")

normal = string.ascii_lowercase
small = "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀꜱᴛᴜᴠᴡxʏᴢ"
trans = str.maketrans(normal, small)

def to_small_caps(text):
    return text.lower().translate(trans)


tk.Label(root, text="Text normal:", fg="white", bg="#2c3e50", font=("Arial", 12, "bold")).pack(pady=(15,5))
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=(0,10))


tk.Label(root, text="Small caps:", fg="white", bg="#2c3e50", font=("Arial", 12, "bold")).pack()
output = tk.Text(root, height=4, width=40, font=("Courier", 12, "bold"), bg="#34495e", fg="white", bd=0)
output.pack(pady=(0,15))

def convert(event=None):
    result = to_small_caps(entry.get())
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)

entry.bind("<KeyRelease>", convert)


def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output.get("1.0", tk.END).strip())
    root.update()
    copy_label.config(text="Copiat ✔")

button = tk.Button(root, text="Copiază", command=copy_text,
                   bg="#1abc9c", fg="white", activebackground="#16a085",
                   font=("Arial", 12, "bold"), bd=0, relief="flat", padx=15, pady=5)
button.pack(pady=5)


def on_enter(e):
    button['bg'] = "#16a085"
def on_leave(e):
    button['bg'] = "#1abc9c"

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

copy_label = tk.Label(root, text="", fg="#f1c40f", bg="#2c3e50", font=("Arial", 10, "bold"))
copy_label.pack(pady=(5,0))

root.mainloop()
