from tkinter import *
window = Tk()

from pyshorteners import *

url = Shortener()

def short_url():
    long_url = url_entry.get()
    shorten_url = url.tinyurl.short(long_url)        # url is an Object Defined in Above cell of Class Shortener
    short_url_entry.insert(0, shorten_url)
    

label = Label(window, text='URL Shortener', font=('Helvetica',15,'bold')).grid(row=1, column=0, columnspan=3)
url_label = Label(window, text='Enter url to be Shorten : ', font=('Helvetica',10,'italic')).grid(row=2, column=0)
url_entry = Entry(window)
url_entry.grid(row=2, column=1, ipadx=20, ipady=5)
label2 = Label(window, text='Shorten url : ', font=('Helvetica',10,'italic')).grid(row=3, column=0)
short_url_entry = Entry(window).grid(row=3, column=1, ipadx=20, ipady=5)
generate_button = Button(window, text='Generate', font=('Helvetica',10,'italic'), command=short_url).grid(row=4, column=0, columnspan=2, ipadx=5, ipady=5)


window.mainloop()
