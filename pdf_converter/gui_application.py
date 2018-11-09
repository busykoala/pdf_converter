from pathlib import Path
from tkinter import Tk, Label, filedialog, Button
import converting_pdf
import os


def main():

    window = Tk()
    window.attributes("-topmost", True)
    window.update()
    window.attributes("-topmost", False)
    window.title("Busykoala PDF converter")

    def convert_file(file_path):
        converting_instance = converting_pdf.PdfConverter(file_path)
        converting_instance.return_errors()
        with filedialog.asksaveasfile(defaultextension='pdf') as output_file:
            output_path = output_file.name
        converting_instance.convert_2_pdf(output_path)

        lbl.configure(text='Thank you for using busykoala converter ;-)')
        btn.destroy()

    def get_file_path():
        entry_path = None
        if not entry_path:
            entry_path = str(Path.home())
            if os.path.isdir(os.path.join(str(Path.home()), 'Documents')):
                entry_path = os.path.join(str(Path.home()), 'Documents')
        file_path = filedialog.askopenfilename(
            initialdir=entry_path,
            title="Select file",
            filetypes=(("Markdown", "*.md"),
                       ("all files", "*.*"))
        )
        if not file_path:
            file_path = "Pick a File in your file browser."
        else:
            lbl.configure(text=file_path.rsplit('/', 1)[1])
            btn.configure(text='Convert and download',
                          command=lambda: convert_file(file_path))

    lbl = Label(window, text="Pick a File in your file browser.")
    lbl.grid(column=1, row=1, ipadx=100, ipady=50)
    lbl.config(font=("Courier", 25))

    btn = Button(window, text="Choose File", command=get_file_path)
    btn.grid(column=1, row=2, padx=100)

    lbl2 = Label(window, text='')
    lbl2.grid(column=1, row=3, ipadx=50, ipady=20)

    window.mainloop()


if __name__ == '__main__':
    main()
