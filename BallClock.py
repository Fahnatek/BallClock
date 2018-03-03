"""
This program takes the time from the user then
displays the time using "balls", advance the time by
pressing the "Up" arrow key.
"""

__author__ = "Joseph Hnatek"
__date__ = "2/16/18"
import turtle


class BallClock:

    def __init__(self, hour, mins):

        if hour < 1 or hour > 12 or mins < 0 or mins > 59:
            print("Invalid time given")
            return

        self.__oneRail = []
        self.__fiveRail = []
        self.__hourRail = []
        self.__reserveRail = []

        numMins = (mins % 5)
        numFive = (mins - numMins) // 5
        numHour = hour
        numReserve = (30 - (numMins + numFive + numHour))

        label = turtle.Turtle()
        label.penup()

        label.goto(-375, 95)
        label.write("1 min", True, "center")
        label.ht()

        pos = 0
        for x in range(numMins):
            t = turtle.Turtle()
            t.shape("circle")
            t.penup()
            t.goto(-350, 100)

            t.forward(pos)
            pos = pos + 25

            self.__oneRail.append(t)

        label.goto(-375, 45)
        label.write("5 min", True, "center")
        label.ht()

        pos = 0
        for x in range(numFive):
            t = turtle.Turtle()
            t.shape("circle")
            t.penup()
            t.goto(-350, 50)

            t.forward(pos)
            pos = pos + 25

            self.__fiveRail.append(t)

        label.goto(-375, -5)
        label.write("hour", True, "center")
        label.ht()

        pos = 0
        for x in range(numHour):
            t = turtle.Turtle()
            t.shape("circle")
            t.penup()
            t.goto(-350, 0)

            t.forward(pos)
            pos = pos + 25

            self.__hourRail.append(t)

        pos = 0
        for x in range(numReserve):
            t = turtle.Turtle()
            t.shape("circle")
            t.penup()
            t.goto(-350, -50)

            t.forward(pos)
            pos = pos + 25

            self.__reserveRail.append(t)

    def advanceTime(self):

        ball = self.__reserveRail.pop(0)

        if len(self.__oneRail) == 0:
            ball.setpos(-350, 100)
        else:
            ball.setpos(self.__oneRail[-1].xcor() + 25, 100)

        self.__oneRail.append(ball)

        for x in self.__reserveRail:
            x.setpos(x.xcor() - 25, -50)

        if len(self.__oneRail) == 5:
            ball = self.__oneRail.pop()
            if len(self.__fiveRail) == 0:
                ball.setpos(-350, 50)
            else:
                ball.setpos(self.__fiveRail[-1].xcor() + 25, 50)
                self.__fiveRail.append(ball)

            while len(self.__oneRail) > 0:
                    ball = self.__oneRail.pop()
                    ball.setpos(self.__reserveRail[-1].xcor() + 25, -50)
                    self.__reserveRail.append(ball)

            if len(self.__fiveRail) == 12:
                ball = self.__fiveRail.pop()
                ball.setpos(self.__hourRail[-1].xcor() + 25, 0)
                self.__hourRail.append(ball)

                while len(self.__fiveRail) > 0:
                    ball = self.__fiveRail.pop()
                    ball.setpos(self.__reserveRail[-1].xcor() + 25, -50)
                    self.__reserveRail.append(ball)

            if len(self.__hourRail) > 12:
                while len(self.__hourRail) > 1:
                    ball = self.__hourRail.pop()
                    ball.setpos(self.__reserveRail[-1].xcor() + 25, -50)
                    self.__reserveRail.append(ball)


def main():

    win = turtle.Screen()
    win.setup(850,400)

    time = win.textinput("text input", "What is the time? XX:XX").split(":")

    clock = BallClock(int(time[0]), int(time[1]))

    win.onkey(clock.advanceTime, "Up")

    win.listen()
    win.exitonclick()


main()

