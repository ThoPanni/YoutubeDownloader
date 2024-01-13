import tkinter as tk
from tkinter import ttk

#Version 0.1

root = tk.Tk()
root.title("YoutubeDownloader by TP")

# Fenstergröße vorgeben
root.geometry("800x400")
root.minsize(width=250, height=250)
root.maxsize(width=1000, height=800)
# root.resizable(width=False, height=False)

label1 = tk.Label(root, text="Label 1", bg="green")
label1.pack(side="top")

# label2 = tk.Label(root, text="Label 2", bg="red")
# label2.pack(side="top", fill="both", expand=True)

label3 = ttk.Label(root, text="Label 3 ttk")
label3.pack()
label3.configure()


def say_hello():
    print("Hello")

def print_entry_input():
    print(entry1.get())

button1 = ttk.Button(root, text="Klick mich", command=say_hello, state=tk.NORMAL)
button1.pack()

for item in button1.keys():
    print(item, ": ", button1[item])

quit_button = ttk.Button(root, text="Schließen", command=root.destroy)
quit_button.pack()

entry1 = ttk.Entry(root)
entry1.pack()

for item in entry1.keys():
    print(item, ": ", entry1[item])

button2 = ttk.Button(root, text="Feldinhalt ausgeben", command=print_entry_input)
button2.pack()

root.mainloop()