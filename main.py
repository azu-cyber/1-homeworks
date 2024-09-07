from tkinter import *
from tkinter import ttk

def calculate(*args):
    if choice.get() == 'meters':
        value = float(inp.get())
        result.set(int(3.281 * value * 10000.0 + 0.5) / 10000.0)
        units.set('feet')
    if choice.get() == 'feet':
        value = float(inp.get())
        result.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        units.set('meters')

root = Tk()
root.title('Length Converter')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe = ttk.Frame(root, padding='25 25 25 25')
mainframe.grid(sticky=(N, W, E, S))

inp = StringVar()
choice = StringVar()
result = StringVar()
units = StringVar()

input_entry = ttk.Entry(mainframe, width=7, textvariable=inp)
input_entry.grid(row=1, column=0)
choices = ttk.Combobox(mainframe, width=10, textvariable=choice, values=('meters', 'feet'))
choices.grid(row=1, column=1)

ttk.Label(mainframe, text='is equal to').grid(row=2, column=0)
ttk.Label(mainframe, textvariable=result).grid(row=2, column=1, sticky=E)
ttk.Label(mainframe, textvariable=units).grid(row=2, column=2, sticky=W)

ttk.Button(mainframe, text='Calculate', command=calculate).grid(row=3, column=1)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
    root.mainloop()