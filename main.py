from tkinter import *
from random import *
from time import *
from math import *

tk = Tk()
screen = Canvas(tk, width = 600, height = 600, background = "black")
screen.pack()

planetSize = [7, 7, 8, 4, 7, 30]
orbitSize = [60, 120, 180, 184, 250, 300]

angles = [0, 212, 123, 123, 180, 230]
orbitingSpeeds = [4.5, 2.5, 1.5, 1.5, 1.7, 0.6]

colors = ["grey90", "hotpink", "red", "orange", "yellow", "green", "cyan3"]
planetDrawing = [0, 0, 0 , 0, 0, 0, 0]
numPlanets = len(orbitSize)

def circle(xC, yC, r, col):
  x1 = xC - r
  y1 = yC - r
  x2 = xC + r
  y2 = yC + r
  return screen.create_oval(x1, y1, x2, y2, fill = col, outline = col)

def drawStars(numStars):
  for i in range(0, numStars):
    xC = randint(0, 600)
    yC = randint(0, 600)
    size = uniform(1, 2)
    drawCircle(x, y, size, "white")