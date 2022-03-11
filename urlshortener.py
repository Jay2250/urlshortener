from tkinter import *
window = Tk()

from pyshorteners import *

url = Shortener()

def short_url():
    long_url = url_entry.get()
    shorten_url = url.tinyurl.short(long_url)        
    short_url_entry.delete(0, END)
    short_url_entry.insert(0, shorten_url)
    

label = Label(window, text='URL Shortener', font=('Helvetica',15,'bold'))
label.grid(row=1, column=0, columnspan=3)
url_label = Label(window, text='Enter url to be Shorten : ', font=('Helvetica',10,'italic'))
url_label.grid(row=2, column=0)
url_entry = Entry(window)
url_entry.grid(row=2, column=1, ipadx=20, ipady=5)
label2 = Label(window, text='Shorten url : ', font=('Helvetica',10,'italic'))
label2.grid(row=3, column=0)
short_url_entry = Entry(window)
short_url_entry.grid(row=3, column=1, ipadx=20, ipady=5)
generate_button = Button(window, text='Generate', font=('Helvetica',10,'italic'), command=short_url)
generate_button.grid(row=4, column=0, columnspan=2, ipadx=5, ipady=5)


window.mainloop()
