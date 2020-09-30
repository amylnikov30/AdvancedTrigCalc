import calculator
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math
import cmd


#class CalculatorUI:
window = Tk()
window.title("TrigCalc")
#window.iconbitmap('icon.ico')
window.geometry("500x500")
color = "#002240"
window.configure(bg=color)
canvas=Canvas(window, height=250, width=500, bg=color, highlightthickness=0)
canvas.pack()
canvas.place(relx = 0, rely = 0.5)
sideLabels = [Label]
angleLabels = [Label]

prevSides = []
prevAngles = []



#console = cmd.Console(window, canvas)


alab = Label(window, text="Side a: ", bg=color)
alab.grid(row=0, column=3)
alab.configure(foreground="white")
blab = Label(window, text="Side b: ", bg=color)
blab.grid(row=1, column=3)
blab.configure(foreground="white")
clab = Label(window, text="Side c: ", bg=color)
clab.grid(row=2, column=3)
clab.configure(foreground="white")
Alab = Label(window, text="Angle A: ", bg=color)
Alab.grid(row=3, column=3)
Alab.configure(foreground="white")
Blab = Label(window, text="Angle B: ", bg=color)
Blab.grid(row=4, column=3)
Blab.configure(foreground="white")
Clab = Label(window, text="Angle C: ", bg=color)
Clab.grid(row=5, column=3)
Clab.configure(foreground="white")

'''
aAns = Label(window, text="", bg=color).grid(row=0, column=5)
bAns = Label(window, text="", bg=color).grid(row=1, column=5)
cAns = Label(window, text="", bg=color).grid(row=2, column=5)
AAns = Label(window, text="", bg=color).grid(row=3, column=5)
BAns = Label(window, text="", bg=color).grid(row=4, column=5)
CAns = Label(window, text="", bg=color).grid(row=5, column=5)
'''

aAns = Label(window)
bAns = Label(window)
cAns = Label(window)
AAns = Label(window)
BAns = Label(window)
CAns = Label(window)

status = Label(window)


aEnt = Entry(window, width=10)
aEnt.grid(row=0, column=4)
bEnt = Entry(window, width=10)
bEnt.grid(row=1, column=4)
cEnt = Entry(window, width=10)
cEnt.grid(row=2, column=4)
AEnt = Entry(window, width=10)
AEnt.grid(row=3, column=4)
BEnt = Entry(window, width=10)
BEnt.grid(row=4, column=4)
CEnt = Entry(window, width=10)
CEnt.grid(row=5, column=4)

'''if a.get().isnumeric():
    a = float(a.get())
if b.get().isnumeric():
    b = float(b.get())
if c.get().isnumeric():
    c = float(c.get())
if A.get().isnumeric():
    A = float(A.get())
if B.get().isnumeric():
    B = float(B.get())
if C.get().isnumeric():
    C = float(C.get())'''

#print(f"Sides: {sides}")
#print(f"Angles: {angles}")
calc = calculator.Calculator
style = ttk.Style()
style.configure("TButton", foreground = "black")

'''def __init__(self):
    float(a)
    float(b)
    float(c)
    float(A)
    float(B)
    float(C)
    sides = [a, b, c]
    angles = [A, B, C]
    calc = calculator.Calculator(a=a, b=b, c=c, A=A, B=B, C=C)'''

'''def findLongest(a, b, c):

    ls = [a, b, c]

    ls.sort()

    return(ls[-1])'''


def drawTriangleLabels(a, b, c, A, B, C):

    # ls = sides[0]
    # ss = sides[2]
    #
    # la = angles[0]
    # ls = angles[]

    sides = [a, b, c]
    angles = [A, B, C]

    sides.sort()
    angles.sort()


    ls = max(sides)
    ss = min(sides)

    la = max(angles)
    sa = min(angles)

    ssLoc = (0, 0)
    osLoc = (0, 0)
    saLoc = (0, 0)
    oaLoc = (0, 0)

    yCoor = 300 * (ss/ls)* math.sin(math.radians(angles[1]))
    xCoor = 300 * (ss/ls) * math.cos(math.radians(angles[1]))

    if math.sqrt((100 - xCoor)**2 + (200 - yCoor)**2) > math.sqrt((400 - xCoor)**2 + (200 - yCoor)**2):
        ssLoc = (400, (yCoor/2))
        osLoc = (100, (yCoor)/2)
        saLoc = (145, 185)
        oaLoc = (345, 185)
    else:
        ssLoc = (100, (yCoor)/2)
        osLoc = (400, (yCoor)/2)
        saLoc = (345, 185)
        oaLoc = (145, 185)

    #print("Small Side Location: ", ssLoc)


    #sides

    lsLabel = canvas.create_text(200, 225, text=str(ls), fill="grey")

    ssLabel = canvas.create_text(ssLoc[0], 200 - ssLoc[1], text=str(ss), fill="grey")

    osLabel = canvas.create_text(osLoc[0], 200 - osLoc[1], text=str(sides[1]), fill="grey")


    #angles

    laLabel = canvas.create_text(100 + xCoor, 200 - yCoor + 35, text=str(round(la, ndigits=4)), fill="grey")

    saLabel = canvas.create_text(saLoc[0], saLoc[1], text=str(round(sa, ndigits=4)), fill="grey")

    oaLabel = canvas.create_text(oaLoc[0], saLoc[1], text=str(round(angles[1], ndigits=4)), fill="grey")


def drawTriangle(a, b, c, A, B, C):
    sides = [a, b, c]
    ls = max([a, b, c])
    ss = min([a, b, c])
    angles = [A, B, C]
    #sides.sort()
    angles.sort()

    yCoor = 300 * (ss/ls)* math.sin(math.radians(angles[1]))
    xCoor = 300 * (ss/ls) * math.cos(math.radians(angles[1]))



    triangle = canvas.create_line(100, 200, 400, 200, xCoor+100, 200 - yCoor, 100, 200, width = 3, fill="grey")

    # print("xCoor: " + str(xCoor))
    # print("yCoor: " + str(yCoor))
    # print(angles)

    #return {"angles" : angles, "sides" : sides.sort()}
    #triangle = canvas.create_line()
    #return (xCoor, yCoor)


'''def draw(a, b, c):
    # determine corner points of triangle with sides a, b, c
    A = (0, 0)
    B = (c, 0)
    hc = (2 * (a**2*b**2 + b**2*c**2 + c**2*a**2) - (a**4 + b**4 + c**4))**0.5 / (2.*c)
    dx = (b**2 - hc**2)**0.5
    if abs((c - dx)**2 + hc**2 - a**2) > 0.01: dx = -dx # dx has two solutions
    C = (dx, hc)

    # move away from topleft, scale up a bit, convert to int
    coords = [int((x + 1) * 50) for x in A+B+C]

    # draw using Tkinter
    #root = Tk()
    #canvas = Canvas(root, width=500, height=300)
    canvas.create_polygon(*coords)
    #canvas.pack()
    #root.mainloop()
'''

def doPreviousEntry(event=None):
    a = prevSides[0]
    b = prevSides[1]
    c = prevSides[2]

    A = prevAngles[0]
    B = prevAngles[1]
    C = prevAngles[2]

    calc = calculator.Calculator(a, b, c, A, B, C);


    try:
        calc.main()
    except:
        messagebox.showerror("Error", "This triangle is not possible")

    global aAns
    global bAns
    global cAns
    global AAns
    global BAns
    global CAns

    global status

    aAns.config(text=calc.a, bg=color, foreground="white")
    bAns.config(text=calc.b, bg=color, foreground="white")
    cAns.config(text=calc.c, bg=color, foreground="white")
    AAns.config(text=calc.A, bg=color, foreground="white")
    BAns.config(text=calc.B, bg=color, foreground="white")
    CAns.config(text=calc.C, bg=color, foreground="white")





    aAns.grid(row=0, column=5)
    bAns.grid(row=1, column=5)
    cAns.grid(row=2, column=5)
    AAns.grid(row=3, column=5)
    BAns.grid(row=4, column=5)
    CAns.grid(row=5, column=5)

    #draw(calc.a, calc.b, calc.c)
    drawTriangle(calc.a, calc.b, calc.c, calc.A, calc.B, calc.C)
    drawTriangleLabels(calc.a, calc.b, calc.c, calc.A, calc.B, calc.C)


#@classmethod
def calculate(event=None):

    clearLabels()
    canvas.delete("all")

    if aEnt.get() != 0 and aEnt.get() != "":
        a = float(aEnt.get())
    else:
        a = 0
    if bEnt.get() != 0 and bEnt.get() != "":
        b = float(bEnt.get())
    else:
        b = 0
    if cEnt.get() != 0 and cEnt.get() != "":
        c = float(cEnt.get())
    else:
        c = 0
    if AEnt.get() != 0 and AEnt.get() != "":
        A = float(AEnt.get())
    else:
        A = 0
    if BEnt.get() != 0 and BEnt.get() != "":
        B = float(BEnt.get())
    else:
        B = 0
    if CEnt.get() != 0 and CEnt.get() != "":
        C = float(CEnt.get())
    else:
        C = 0
    sides = [a, b, c]
    angles = [A, B, C]
    calc = calculator.Calculator(a=a, b=b, c=c, A=A, B=B, C=C)

    prevSides.append(a)
    prevSides.append(b)
    prevSides.append(c)

    prevAngles.append(A)
    prevAngles.append(B)
    prevAngles.append(C)

    try:
        calc.main()
    except:
        messagebox.showerror("Error", "This triangle is not possible")
        #print("Errored out")
        #clearAll(event=None)


    global aAns
    global bAns
    global cAns
    global AAns
    global BAns
    global CAns

    global status

    aAns.config(text=calc.a, bg=color, foreground="white")
    bAns.config(text=calc.b, bg=color, foreground="white")
    cAns.config(text=calc.c, bg=color, foreground="white")
    AAns.config(text=calc.A, bg=color, foreground="white")
    BAns.config(text=calc.B, bg=color, foreground="white")
    CAns.config(text=calc.C, bg=color, foreground="white")





    aAns.grid(row=0, column=5)
    bAns.grid(row=1, column=5)
    cAns.grid(row=2, column=5)
    AAns.grid(row=3, column=5)
    BAns.grid(row=4, column=5)
    CAns.grid(row=5, column=5)

    #draw(calc.a, calc.b, calc.c)
    drawTriangle(calc.a, calc.b, calc.c, calc.A, calc.B, calc.C)
    drawTriangleLabels(calc.a, calc.b, calc.c, calc.A, calc.B, calc.C)

    #status = Label(window, bg=color, foreground="green")
    status.grid(row=7, column=4)


    if calc.enoughInfo == True:
        status.config(bg=color, foreground="green", text="Successfully Calculated")
    else:
        messagebox.showerror("Error", "Not enough information provided to calculate.\nPlease check all fields.")
        clearAll()




    '''for i in range(len(calc.sides)):
        #Label(window, text="", bg=color, foreground=color).grid(row=i, column=5)
        sideLabels.append(Label(window, text=str(calc.sides[i]), bg=color, foreground="white").grid(row=i, column=5))

    for i in range(len(calc.angles)):
        angleLabels.append(Label(window, text=str(calc.angles[i]), bg=color, foreground="white").grid(row=i+3, column=5))
    '''







def clearLabels(event=None):
    aAns.config(text="")
    bAns.config(text="")
    cAns.config(text="")
    AAns.config(text="")
    BAns.config(text="")
    CAns.config(text="")
    status.config(text="")



def clearEntries(event=None):
    aEnt.delete(0, 'end')
    bEnt.delete(0, 'end')
    cEnt.delete(0, 'end')
    AEnt.delete(0, 'end')
    BEnt.delete(0, 'end')
    CEnt.delete(0, 'end')


def clearAll(event=None):
    clearLabels()
    clearEntries()
    canvas.delete("all")






'''for i in range(len(calc.sides)):
    Label(window, text=str(calc.sides[i]), bg=color, foreground="white").grid(row=i, column=3)

for i in range(len(calc.angles)):
    Label(window, text=str(calc.angles[i]), bg=color, foreground="white").grid(row=i+3, column=3)
'''



window.bind("<Return>", calculate)
window.bind("<Control-w>", clearAll)
window.bind("<Control-r>", doPreviousEntry)
#console.console.bind("<Return>", console)


calcBtn = ttk.Button(window, text="Calculate", command=calculate)
calcBtn.grid(row=6, column=4)

clearBtn = ttk.Button(window, text = "Clear", command=clearAll)
clearBtn.grid(row=6, column=5)

calcPrevBtn = ttk.Button(window, text = "Calculate Previous", command=doPreviousEntry)
calcPrevBtn.grid(row=6, column=6)





#Trig command line
#----------------------------------------------------------------


'''def console(event=None):

    global console

    console.run()'''


'''cmdEntry = Entry(window, width=300)
cmdEntry.grid(row=10, column=0)

cmd = cmdEntry.get()
output = str
def sendCmd():
    global cmd
    global output
    output = os.popen(cmd)


Label(window, text=output, bg=color, foreground="white").grid(row=11, column=4)
ttk.Button(window, text="Submit").grid(row=10, column=10)
'''
#window.mainloop()
