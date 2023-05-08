import tkinter as tk
from PIL import Image
import pystray
import time

icon = Image.open('icon.png')

def show_window():
    root.deiconify()

def quit_app():
    root.quit()

def minimize():
    root.withdraw() # Ocultar la ventana de tkinter
    menu = pystray.Menu(pystray.MenuItem('Abrir', show_window), pystray.MenuItem('Salir', quit_app))
    tray_icon = pystray.Icon('nombre_icono', icon,  'Mensaje de tooltip', menu)
    tray_icon.run()


root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')
label = tk.Label(root, text="Safe eyes for windows is coming!", font=("Helvetica", 27), fg="white", bg="black")
label.pack(expand=True)
label.place(relx = 0.5, rely = 0.45, anchor = 'center')
button = tk.Button(root, text = "Skip", command = minimize, font = ("Helvetica", 15))
button.pack()
button.place(relx = 0.5, rely = 0.55, anchor = 'center')

root.mainloop()