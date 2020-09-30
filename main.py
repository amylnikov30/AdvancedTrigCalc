from calculatorUI import *


def _quit(event=None):
    exit(0)

window.bind("<Control-q>", _quit)
window.bind("<Escape>", _quit)

#window.iconbitmap('icon.ico')

window.mainloop()
