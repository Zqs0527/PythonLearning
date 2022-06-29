from logging import root
import tkinter

def mouse_click(event):
    # retrieve x,y coordinates as a tuple
    coords = root.winfo_pointerxy()
    print('coords: {}'.format(coords))
    print('X: {}'.format(coords[0]))
    print('X: {}'.format(coords[1]))

root = tkinter.Tk()
root.bind('<Button>', mouse_click)
root.mainloop()