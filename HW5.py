#Problem 1
def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print(x)


def main():
    k = float(input("Enter k: "))
    x = float(input("Enter x: "))
    n = int(input("Enter number of iterations: "))

    chaos(k, x, n)


main()

#Problem 2
def kToF(k):
    return (k -273) * 9/5 + 32

def main():
    print("Kelvin\tFahrenheit")

    for k in range(0, 301, 20):
        f = kToF(k)
        print(k, "\t", f)

main()

#Problem 3
def calcPmt(P0, r, k, N):
    d = P0 / ((1 - (1 + r / k) ** (-N * k)) / (r / k))
    return d


def main():
    P0 = float(input("Enter amount to finance: "))
    r = float(input("Enter annual interest rate as a decimal: "))
    k = int(input("Enter number of times interest is compounded per year: "))
    N = int(input("Enter number of years: "))

    payment = calcPmt(P0, r, k, N)

    print("Monthly payment:", payment)


main()

#Problem 4
from graphics import *
import math


def drawPolygon(n, radius, center):
    angle = 360 / n
    vertices = []

    for i in range(n):
        current_angle = math.radians(i * angle)

        x = center.getX() + radius * math.cos(current_angle)
        y = center.getY() - radius * math.sin(current_angle)

        vertices.append(Point(x, y))

    polygon = Polygon(vertices)
    return polygon


def graphPolygon(win, entry):
    click = win.getMouse()

    n = int(entry.getText())

    center = Point(250, 250)
    radius = 150

    polygon = drawPolygon(n, radius, center)
    polygon.draw(win)


def main():
    win = GraphWin("Polygon", 500, 500)

    label = Text(Point(100, 30), "Number of sides:")
    label.draw(win)

    entry = Entry(Point(200, 30), 10)
    entry.draw(win)

    button = Rectangle(Point(300, 15), Point(400, 45))
    button.draw(win)

    button_text = Text(Point(350, 30), "Graph")
    button_text.draw(win)

    graphPolygon(win, entry)

    button_text.setText("Exit")

    win.getMouse()
    win.close()


main()

#problem 5
from graphics import *
import math
def logistic(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)

    return x


def problem5():
    x = float(input("Enter the initial value: "))
    k = float(input("Enter k: "))

    win = GraphWin("Logistic Function", 600, 500)

    
    x_axis = Line(Point(50, 450), Point(550, 450))
    y_axis = Line(Point(50, 450), Point(50, 50))

    x_axis.draw(win)
    y_axis.draw(win)

    
    for n in range(100):
        y = logistic(k, x, n)

        screen_x = 50 + n * 5
        screen_y = 450 - y * 400

        point = Point(screen_x, screen_y)
        point.draw(win)

    win.getMouse()
    win.close()

problem5()