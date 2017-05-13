import tkinter # for Python 3

class form:
    def on_click_1(e):
        print(e1.get())
        print(e2.get())

    tk = tkinter.Tk()
    tkinter.Label(tk,text="Infected").grid(row =0)
    tkinter.Label(tk,text="Vaccinated").grid(row =1)

    e1 = tkinter.Entry(tk)
    e2 = tkinter.Entry(tk)
    e1.grid(row =0,column=1)
    e2.grid(row=1,column=1)

    myButton = tkinter.Button(tk, text="Enter",command=tk.quit)

    # this first add is not required in this example, but it's good form.
    myButton.bind("<Button>", on_click_1, add="+")
    myButton.grid(row = 2,column=1)
    # this add IS required for on_click_1 to remain in the handler list

    tk.mainloop()
