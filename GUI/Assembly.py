import tkinter
from operator import add, sub

def drawAssembly(toplayer, nRows, rodPitch, rFuel, rGap, rClad):
    asmPitch = rodPitch * (nRows + 1)
    asm = tkinter.Canvas(toplayer, bg="gray", height=asmPitch, width=asmPitch)


    pinOrigin = [0, 0]
    rFuelCoord = rFuel, rFuel
    rGapCoord  = rGap,  rGap
    rCladCoord = rClad, rClad
    for i in range(nRows):
        pinOrigin[0] += rodPitch
        pinOrigin[1] = 0
        for j in range(nRows):
            pinOrigin[1] += rodPitch
            clad = asm.create_oval(map(add, pinOrigin, rCladCoord), map(sub, pinOrigin, rCladCoord), fill="black", width=0)
            gap = asm.create_oval(map(add, pinOrigin, rGapCoord), map(sub, pinOrigin, rGapCoord), fill="white", width=0)
            fuelPin = asm.create_oval(map(add, pinOrigin, rFuelCoord), map(sub, pinOrigin, rFuelCoord), fill="red", width=0)

    return asm