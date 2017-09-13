from tkinter import *
from ttk import *
from Assembly import drawAssembly

root = Tk()
root.title('Rx Creator')
#root.geometry('800x500')

master = Frame(root, name='master') # create Frame in "root"
master.pack(fill=BOTH) # fill both sides of the parent

nb = Notebook(master, name='nb')
nb.pack(fill=BOTH, padx=2, pady=3)

CoreFrame = Frame(master, name="core-frame")
CoreFrame.pack()
nb.add(CoreFrame, text="Core")

AssemblyFrame = Frame(nb, name="assembly-frame")
AssemblyFrame.pack()
nb.add(AssemblyFrame, text="Assembly")


#Example values for assembly
nRows = 15
pitch = 25
rFuel = 5
rGap = 7
rClad = 10

#Left Frame
leftframe = Frame(AssemblyFrame)
leftframe.pack(side=LEFT)
Assembly = drawAssembly(leftframe, nRows, pitch, rFuel, rGap, rClad)
Assembly.pack(side=TOP)

#Right Frame
rightframe = Frame(AssemblyFrame)
rightframe.pack(side=RIGHT)

#Entry 1 Frame
entry1frame = Frame(rightframe)
entry1frame.pack( side=TOP)
L1 = Label(entry1frame, text="Number of Pins Per Row")
L1.pack( side = TOP)
E1 = Entry(entry1frame)
E1.pack(side = BOTTOM)

#Entry 2 Frame
entry2frame = Frame(rightframe)
entry2frame.pack( side=TOP)
L2 = Label(entry2frame, text="Fuel Pin Pitch")
L2.pack( side = TOP)
E2 = Entry(entry2frame)
E2.pack(side = BOTTOM)

#Entry 3 Frame
entry3frame = Frame(rightframe)
entry3frame.pack( side=TOP)
L3 = Label(entry3frame, text="Fuel Pin Radius")
L3.pack( side = TOP)
E3 = Entry(entry3frame)
E3.pack(side = BOTTOM)

#Entry 4 Frame
entry4frame = Frame(rightframe)
entry4frame.pack( side=TOP)
L4 = Label(entry4frame, text="Gap Radius")
L4.pack( side = TOP)
E4 = Entry(entry4frame)
E4.pack(side = BOTTOM)

#Entry 5 Frame
entry5frame = Frame(rightframe)
entry5frame.pack( side=TOP)
L5 = Label(entry5frame, text="Cladding Radius")
L5.pack( side = TOP)
E5 = Entry(entry5frame)
E5.pack(side = BOTTOM)

#Update Function
def update():
    global Assembly
    global nRows
    global pitch
    global rFuel
    global rGap
    global rClad

    if E1.get():
        nRows = int(E1.get())
    if E2.get():
        pitch = float(E2.get())
    if E3.get():
        rFuel = float(E3.get())
    if E4.get():
        rGap  = float(E4.get())
    if E5.get():
        rClad = float(E5.get())

    Assembly.pack_forget()
    Assembly = drawAssembly(leftframe, nRows, pitch, rFuel, rGap, rClad)
    Assembly.pack(side=TOP)

#Button Frame
buttonframe = Frame(rightframe)
buttonframe.pack(side=TOP)
B = Button(buttonframe, text="OK", command=update)
B.pack()


root.mainloop()