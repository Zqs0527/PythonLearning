import tkinter
import time

# handler for timer event
def alarm():
    print('Calling the pizza company..')

# handler for ringing doorbell
def doorbell():
    print('Ding dong')
    time.sleep(4)
    print('Opening the door')

# handler when the phone rings
def phonecall():
    print('Answering the phone')


root = tkinter.Tk()

# create buttons
tkinter.Button(root, text='Ring Doorbell', command=doorbell).pack()
tkinter.Button(root, text='Call phone', command=phonecall).pack()

# set a timer for 4s
root.after(4000, alarm)

# start the event loop
root.mainloop()
