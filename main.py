from tkinter import *
import random
from time import *
from math import *
from tkinter.tix import *

tk = Tk()
screen = Canvas(tk, width = 600, height = 600, background = "Black")
screen.pack()

class planet:
  def __init__(self, size, orbit, init_angle, speed, color):
    self.size = size
    self.orbit = orbit
    self.angle = init_angle
    self.speed = speed
    self.color = color
    
planetList = []


planetSize = [7, 7, 8, 4, 7, 30]
orbitSize = [60, 120, 180, 184, 250, 300]

angles = [0, 212, 123, 123, 180, 230]
orbitingSpeeds = [15, 20, 14, 13, 10, 7]

colors = ["grey90", "hotpink", "red", "orange", "yellow", "green", "cyan3"]
planetDrawing = []
numPlanets = len(orbitSize)

for i in range(numPlanets):
 p = planet(random.randint(8, 20), random.randint(60, 300),random.randint(0, 360), random.uniform(1, 5), colors[random.randint(0, len(colors) -1)])
 planetList.append(p)
 planetDrawing.append(0) 
  
def drawCircle(xC, yC, r, col):
  x1 = xC - r
  y1 = yC - r
  x2 = xC + r
  y2 = yC + r
  return screen.create_oval(x1, y1, x2, y2, fill = col, outline = col)

def drawStars(numStars):
  for i in range(0, numStars):
    x = random.randint(0, 600)
    y = random.randint(0, 600)
    size = random.uniform(1, 2)
    drawCircle(x, y, size, "white")

def drawSun(xC, yC, sunRadius):
  drawCircle(xC, yC, sunRadius, "yellow")

def drawPlanets(xSun, ySun, degAngle, orbitalRadius, planetSize, color, fx, fy):
  radianAngle = radians(degAngle)
  xPlanet = xSun + orbitalRadius * fx(radianAngle)
  yPlanet = ySun - orbitalRadius * fy(radianAngle)
  return drawCircle(xPlanet, yPlanet, planetSize, color)

def animateSolarSystem(numStars, xSun, ySun, fx, fy):
  drawStars(numStars)
  
  drawSun(xSun, ySun, 35)
  
  while True:
    for i in range(numPlanets):
      planetDrawing[i] = drawPlanets(xSun, ySun,             planetList[i].angle, planetList[i].orbit, planetList[i].size, planetList[i]. color, fx, fy)
      planetList[i].angle = planetList[i].angle + planetList[i].speed
    screen.update()
    sleep(.03)
    for i in range(numPlanets):
      screen.delete(planetDrawing[i])
class window(Frame):
  def __init__(self, master = None):
    Frame.__init__ (self, master)
    self.master = master
    self.pack(fill = BOTH, expand = 1)

animateSolarSystem(0, 300, 300, sin, cos)
tk.mainloop()