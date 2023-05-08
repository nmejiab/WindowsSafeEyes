import tkinter as tk

def minimizar():
    root.iconify()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')
label = tk.Label(root, text="Safe eyes for windows is coming!", font=("Helvetica", 27), fg="white", bg="black")
label.pack(expand=True)
label.place(relx = 0.5, rely = 0.45, anchor = 'center')
button = tk.Button(root, text = "Skip", command = minimizar, font = ("Helvetica", 15))
button.pack()
button.place(relx = 0.5, rely = 0.55, anchor = 'center')
root.mainloop()