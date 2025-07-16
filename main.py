from tkinter import *
from tkinter import ttk

class FeetToMeters:

    def __init__(self, root):
        
        root.title("Calculator Suhu")

        frame = ttk.Frame(root, padding = 100)
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        label1 = ttk.Label(frame, text="Selamat Datang di Calculator", anchor="center")
        label1.grid(column=0, row=0, pady=(0,10), sticky="EW")

        
        label2 = ttk.Label(frame, text="Pilih Jenis Konversi Yang diinginkan", anchor="center")
        label2.grid(column=0, row=1, sticky="EW")
        
        label2 = ttk.Label(frame, text="FROM :", anchor="center")
        label2.grid(column=0, row=2, sticky="EW")

        #-------------------------------------------------------------

        self.from1_radio = StringVar()

        celc = ttk.Radiobutton(frame, text='Celcius', variable=self.from1_radio, value='c')
        celc.grid(column=0, row=3, sticky="W")  

        far = ttk.Radiobutton(frame, text='Farenheit', variable=self.from1_radio, value='f')
        far.grid(column=0, row=4, sticky="W")  

        kelv = ttk.Radiobutton(frame, text='Kelvin', variable=self.from1_radio, value='k')
        kelv.grid(column=0, row=5, sticky="W")  

        rea = ttk.Radiobutton(frame, text='Reamur', variable=self.from1_radio, value='r')
        rea.grid(column=0, row=6, sticky="W")  

        label2 = ttk.Label(frame, text="FROM :", anchor="center")
        label2.grid(column=0, row=2, sticky="EW")

        self.from1 = StringVar()
        entry = ttk.Entry(frame, textvariable=self.from1, justify="center")
        entry.grid(column=1, row=2)

         #-------------------------------------------------------------

        self.to2 = StringVar()

        celc2 = ttk.Radiobutton(frame, text='Celcius', variable=self.to2, value='c')
        celc2.grid(column=0, row=8, sticky="W")  

        far2 = ttk.Radiobutton(frame, text='Farenheit', variable=self.to2, value='f')
        far2.grid(column=0, row=9, sticky="W")  

        kelv2 = ttk.Radiobutton(frame, text='Kelvin', variable=self.to2, value='k')
        kelv2.grid(column=0, row=10, sticky="W")  

        rea2 = ttk.Radiobutton(frame, text='Reamur', variable=self.to2, value='r')
        rea2.grid(column=0, row=11, sticky="W")  

        label3 = ttk.Label(frame, text="TO :", anchor="center")
        label3.grid(column=0, row=7, sticky="EW")

        self.out = StringVar()
        label4 = ttk.Label(frame, textvariable=self.out, anchor="center")
        label4.grid(column=1, row=7, sticky="EW")

        #-------------------------------------------------------------

        cek = ttk.Button(frame, text="KONVERSIKAN", command=self.convert)
        cek.grid(column=0, row=13)

    def convert(self, *args):
        try:
            dari = self.from1_radio.get()
            ke = self.to2.get()
            nilai = float(self.from1.get())

            hasil = 0

            if dari == 'c':
                c = nilai
            elif dari == 'f':
                c = (nilai - 32) * 5/9
            elif dari == 'k':
                c = nilai - 273.15
            elif dari == 'r':
                c = nilai * 5/4
            else:
                self.out.set("Satuan FROM salah")
                return
            
            if ke == 'c':
                hasil = c
            elif ke == 'f':
                hasil = c * 9/5 + 32
            elif ke == 'k':
                hasil = c + 273.15
            elif ke == 'r':
                hasil = c * 4/5
            else:
                self.out.set("Satuan TO salah")
                return

            self.out.set(f"{round(hasil, 2)}")  

        except ValueError:
            self.out.set("Input tidak valid")


root = Tk()

FeetToMeters(root)
root.mainloop()