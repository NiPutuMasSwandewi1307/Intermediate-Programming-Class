import tkinter
home_page = tkinter.Tk()

def tekan() :
    label2 = tkinter.Label(home_page, text="Uhuyy")
    label2.pack()

label = tkinter.Label(home_page, text="Hallo saya sedang berusaha\n Ganbatte!!!")
tombol = tkinter.Button(home_page, text="Ngokeyyy", command=tekan)

label.pack()
tombol.pack()

home_page.mainloop()