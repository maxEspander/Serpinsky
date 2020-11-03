import tkinter as tk
import random as rnd

HEIGHT = 600
WIDTH = 800
NUMBEROFPOINTS = 4

xpoints, ypoints = [], []

def drawpoints():
    global xpoints, ypoints
    xpoints = [rnd.randint(1, WIDTH) for i in range(NUMBEROFPOINTS)]
    ypoints = [rnd.randint(1, HEIGHT) for i in range(NUMBEROFPOINTS)]
    for i in range(NUMBEROFPOINTS):
        canvas.create_oval(xpoints[i] - 2, ypoints[i] - 2, xpoints[i] + 2, ypoints[i] + 2, fill='red')
        canvas.pack()
    print(xpoints, ypoints)

def drawNextPoint(point, rgb = 'black'):
    canvas.create_line(point[0] + 1, point[1] + 1, point[0], point[1], fill=rgb)
    canvas.pack()

def clearCanvas_event(event):
    global canvasTxt
    canvas.delete(tk.ALL)
    canvasTxt = canvas.create_text(60, 10, text='Count of Iterations: ', anchor = 'nw')
    drawpoints()
    beginpoint = initStartPoint(xpoints, ypoints)
    drawNextPoint(beginpoint)

def startSerpinsky_event(event):
    curPoint = beginpoint
    rgb = fromRGB((rnd.randint(1,255), rnd.randint(1,255), rnd.randint(1,255)))
    for i in range(20001):
        rndPointIndex = rnd.randint(0, NUMBEROFPOINTS - 1)
        x = curPoint[0] + (xpoints[rndPointIndex] - curPoint[0]) / 2
        y = curPoint[1] + (ypoints[rndPointIndex] - curPoint[1]) / 2
        drawNextPoint([x, y], rgb)
        curPoint = [x, y]
        if i % 500 == 0:
            iterations = str(i)
            canvas.itemconfigure(canvasTxt, text= 'Count of iterations: ' + iterations)
            canvas.update()


def initStartPoint(x, y):
    xsort = x.copy()
    xsort.sort()
    ysort = y.copy()
    ysort.sort()
    retPoint = [rnd.randint(xsort[0], xsort[2]), rnd.randint(ysort[0], ysort[2])]
    return retPoint

def fromRGB(rgb):
    return '#%02x%02x%02x' % rgb

#xpoints = [rnd.randint(1, WIDTH) for i in range(3)]
#ypoints = [rnd.randint(1, HEIGHT) for i in range(3)]

root = tk.Tk()
btnNew = tk.Button(root, width=50, text='new points')
btnNew.bind('<Button-1>', clearCanvas_event)
btnNew.pack(side=tk.TOP)

btnStart = tk.Button(root, text='сreate Serpinsky', width=50)
btnStart.bind('<Button-1>', startSerpinsky_event)
btnStart.pack(side=tk.TOP)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvasTxt = canvas.create_text(60, 10, text='Count of Iterations: ', anchor = 'nw')
canvas.pack(fill = tk.BOTH)

root.geometry(str(WIDTH) + 'x' + str(HEIGHT + 40))
drawpoints()
beginpoint = initStartPoint(xpoints, ypoints)
print(beginpoint)
drawNextPoint(beginpoint)
root.mainloop()