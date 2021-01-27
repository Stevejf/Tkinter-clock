import time
import tkinter as tk


def tick(time1=''):
    time2 = time.strftime('%I:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)
root = tk.Tk()
root.title("TK Clock 12h Time")
root.geometry("300x60")
clock = tk.Label(root, font=('arial', 30, 'bold'), bg='purple')
clock.pack(fill='both',
           expand=1)
tick()
root.mainloop()