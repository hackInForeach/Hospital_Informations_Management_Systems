from tkinter import *

def credits_press(window, fulwidth, fulheight):
    credit_subwin = Toplevel(window)
    credit_subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/HIMS Icon.png")
    credit_subwin.iconphoto(False, icon)
    credit_subwin.title("Credits")
    Frame(credit_subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth, height=fulheight)

    Label(credit_subwin, bg='deep sky blue', fg='white', text='2205314017 - Doğukan Öztürk', anchor='w', font=("Ariel",
                                                                                                            20, 'bold')).place(x=100, y=100, width=fulwidth-200, height = 50)


    Label(credit_subwin, bg='deep sky blue', fg='red', text='Nesne Tabanlı Programlama Projesi', font=("Ariel", 30,
                                                                                             'bold')).place(
        x=fulwidth/4*3-300, y=fulheight/2-50, width=700, height = 70)



    