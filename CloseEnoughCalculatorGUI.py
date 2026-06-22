import tkinter as tk


print ("hello")


myNumber = 0
window = tk.Tk()
window.title("Close Enough Calculator")
window.geometry("300x300")
def button_clicked():
    global myNumber
    myNumber = myNumber + 1
    tk.Label(window,text=myNumber)
    label.config(text = myNumber)
    print(myNumber)

turn_on = tk.Button(window, text="ON", command=button_clicked)
turn_on.pack()

label = tk.Label(window,text="Hello, World!")
label.pack()

window.mainloop()