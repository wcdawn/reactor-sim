import tkinter
from Assembly import drawAssembly

top = tkinter.Tk()
top.title('Rx Creator')
top.geometry('800x500')

#Example values
nRows = 15
pitch = 25
rFuel = 5
rGap = 7
rClad = 10

#Left Frame
leftframe  = tkinter.Frame(top)
leftframe.pack( side=tkinter.LEFT)
Assembly = drawAssembly(leftframe, nRows, pitch, rFuel, rGap, rClad)
Assembly.pack(side=tkinter.TOP)

#Right Frame
rightframe = tkinter.Frame(top)
rightframe.pack( side=tkinter.RIGHT )

#Entry 1 Frame
entry1frame = tkinter.Frame(rightframe)
entry1frame.pack( side=tkinter.TOP)
L1 = tkinter.Label(entry1frame, text="Number of Pins Per Row")
L1.pack( side = tkinter.TOP)
E1 = tkinter.Entry(entry1frame)
E1.pack(side = tkinter.BOTTOM)

#Entry 2 Frame
entry2frame = tkinter.Frame(rightframe)
entry2frame.pack( side=tkinter.TOP)
L2 = tkinter.Label(entry2frame, text="Fuel Pin Pitch")
L2.pack( side = tkinter.TOP)
E2 = tkinter.Entry(entry2frame)
E2.pack(side = tkinter.BOTTOM)

#Entry 3 Frame
entry3frame = tkinter.Frame(rightframe)
entry3frame.pack( side=tkinter.TOP)
L3 = tkinter.Label(entry3frame, text="Fuel Pin Radius")
L3.pack( side = tkinter.TOP)
E3 = tkinter.Entry(entry3frame)
E3.pack(side = tkinter.BOTTOM)

#Entry 4 Frame
entry4frame = tkinter.Frame(rightframe)
entry4frame.pack( side=tkinter.TOP)
L4 = tkinter.Label(entry4frame, text="Gap Radius")
L4.pack( side = tkinter.TOP)
E4 = tkinter.Entry(entry4frame)
E4.pack(side = tkinter.BOTTOM)

#Entry 5 Frame
entry5frame = tkinter.Frame(rightframe)
entry5frame.pack( side=tkinter.TOP)
L5 = tkinter.Label(entry5frame, text="Cladding Radius")
L5.pack( side = tkinter.TOP)
E5 = tkinter.Entry(entry5frame)
E5.pack(side = tkinter.BOTTOM)

#Update Function
def update():
    nRows = int(E1.get())
    pitch = float(E2.get())
    rFuel = float(E3.get())
    rGap  = float(E4.get())
    rClad = float(E5.get())
    global Assembly
    Assembly.pack_forget()
    Assembly = drawAssembly(leftframe, nRows, pitch, rFuel, rGap, rClad)
    Assembly.pack(side=tkinter.TOP)

#Button Frame
buttonframe = tkinter.Frame(rightframe)
buttonframe.pack(side=tkinter.TOP)
B = tkinter.Button(buttonframe, text="OK", command=update)
B.pack()


top.mainloop()