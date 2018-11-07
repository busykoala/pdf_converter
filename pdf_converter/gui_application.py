import os
from pathlib import Path
from tkinter import Tk, Label, filedialog, Button


def main():

    window = Tk()
    window.attributes("-topmost", True)
    window.update()
    window.attributes("-topmost", False)
    window.title("Busykoala PDF converter")

    def get_filename():
        entry_path = None
        if not entry_path:
            entry_path = str(Path.home())
            if os.path.isdir(os.path.join(str(Path.home()), 'Documents')):
                entry_path = os.path.join(str(Path.home()), 'Documents')
        filename = filedialog.askopenfilename(
            initialdir=entry_path,
            title="Select file",
            filetypes=(("PDF files", "*.pdf"),
                       ("all files", "*.*"))
        )
        if not filename:
            filename = "Pick a File in your file browser."
        lbl.configure(text=filename)

    lbl = Label(window, text="Pick a File in your file browser.")
    lbl.grid(column=1, row=1, ipadx=100, ipady=50)
    lbl.config(font=("Courier", 25))

    btn = Button(window, text="Choose File", command=get_filename)
    btn.grid(column=1, row=2, padx=100)

    lbl2 = Label(window, text='')
    lbl2.grid(column=1, row=3, ipadx=50, ipady=20)

    window.mainloop()


if __name__ == '__main__':
    main()
