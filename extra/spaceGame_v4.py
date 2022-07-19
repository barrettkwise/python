import turtle
import time

screen = turtle.Screen()

def gameloop():
        p1.clear()
        p2.clear()

        p1.move()
        for b in p1.bullets:
            b.move()

        p2.move()
        for b in p2.bullets:
            b.move()

        p1.turtle.fd(1)
        p2.turtle.fd(1)
     
        p1.drawShip()
        for b in p1.bullets:
            b.drawBullet()
        
        p2.drawShip()
        for b in p2.bullets:
            b.drawBullet()
        
        if p1.isAccelerating:
             p1.speed += 1
        p1.turtle.fd(p1.speed)

        if p2.isAccelerating:
            p2.speed += 1
        p2.turtle.fd(p2.speed)
        
        turtle.update() # refresh screen
        screen.ontimer(gameloop, 20)

def wPressed():
    p1.isAccelerating = True
 
def wReleased():
    p1.isAccelerating = False

def upArrowPressed():
    p2.isAccelerating = True
 
def upArrowReleased():
    p2.isAccelerating = False

class Player:
    MAX_SPEED = 10
    ROTATION_SPEED = 5
    MAX_BULLETS = 10
    
    def __init__(self, color, position, heading):
        self.isAlive = True
        self.isReadyToFire = True
        self.isAccelerating = False
        self.isTurningLeft = False
        self.isTurningRight = False
        self.speed = 0
        self.color = color
        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.speed(0)
        self.turtle.setpos(position)
        self.turtle.setheading(heading)
        self.bullets = list()
        
    def move(self):
        # Rotate
        if self.isTurningLeft:
            self.turtle.left(Player.ROTATION_SPEED)
        if self.isTurningRight:
            self.turtle.right(Player.ROTATION_SPEED)
 
        # Accelerate
        if self.isAccelerating:
            self.speed += 0.5
        else:
            self.speed -= 0.5
        
        if self.speed > Player.MAX_SPEED:
            self.speed = Player.MAX_SPEED
        elif self.speed < 0:
            self.speed = 0

        # Move Forward
        self.turtle.fd(self.speed)

    def fire(self):
        if not self.isAlive : return

        self.bullets.append(Bullet(self))
        if len(self.bullets) > Player.MAX_BULLETS:
            self.bullets[0].turtle.clear()
            self.bullets.pop(0)
        
    def clear(self):
        self.turtle.clear()
        for b in self.bullets:
            b.turtle.clear()

    def drawShip(self):
        if not self.isAlive : return

        t = self.turtle
        startPos = t.pos()
        startHeading = t.heading()

        # DRAW BODY
        t.fillcolor(self.color)
        t.pencolor(self.color);
        t.begin_fill()
        t.pu()
        t.fd(15)
        t.pd()
        t.rt(30 + 120)
        t.fd(40)
        t.rt(120)
        t.fd(40)
        t.rt(120)
        t.fd(40)
        t.end_fill()

        # RESET TURTLE
        t.pu()
        t.setpos(startPos)
        t.setheading(startHeading)
        
        # DRAW COCKPIT
        t.fillcolor("black")
        t.pencolor("black");
        t.begin_fill()
        t.pu()
        t.fd(3)
        t.lt(90)
        t.pd()
        t.circle(6)
        t.end_fill()

        # RESET TURTLE
        t.pu()
        t.setpos(startPos)
        t.setheading(startHeading)

class Bullet:
    SPEED = 100
 
    def __init__(self, owner):
        self.owner = owner
        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.speed(0)
        self.turtle.setpos(owner.turtle.pos())
        self.turtle.setheading(owner.turtle.heading())
 
    def move(self):
        steps = 10
        stepSpeed = Bullet.SPEED / steps

        if self.owner == p1 : enemy = p2
        else : enemy = p1

        for i in range(steps):
            self.turtle.fd(stepSpeed)
        
        if self.hittest(enemy) :
                print("Game Over!")
                enemy.isAlive = False

    def hittest(self, other):
        return self.turtle.distance(other.turtle) < 10
 
    def drawBullet(self):
        t = self.turtle
        startPos = t.pos()
        startHeading = t.heading()
        t.fillcolor("white")
        t.pencolor("white")
        t.begin_fill()
        t.pd()
        t.fd(1)
        t.lt(90)
        t.circle(2)
        t.end_fill()
        
        t.pu()
        t.setpos(startPos)
        t.setheading(startHeading)

# Player 1 Event Handlers
def wPressed(): p1.isAccelerating = True
def wReleased(): p1.isAccelerating = False
def aPressed(): p1.isTurningLeft = True
def aReleased(): p1.isTurningLeft = False
def dPressed(): p1.isTurningRight = True
def dReleased(): p1.isTurningRight = False
def spacePressed() :
    if p1.isReadyToFire :
        p1.fire()
        p1.isReadyToFire = False
def spaceReleased() : p1.isReadyToFire = True
 
# Player 2 Event Handlers
def upArrowPressed(): p2.isAccelerating = True
def upArrowReleased(): p2.isAccelerating = False
def leftArrowPressed(): p2.isTurningLeft = True
def leftArrowReleased(): p2.isTurningLeft = False
def rightArrowPressed(): p2.isTurningRight = True
def rightArrowReleased(): p2.isTurningRight = False
def mouseClicked(x, y): p2.fire()

screen.bgcolor("black")

p1 = Player("blue", (-200, -200), 90)
p2 = Player("red", (200, 200), 270)

p1.turtle.fd(p1.speed)
p2.turtle.fd(p2.speed)

turtle.tracer(0, 0) # disable automatic screen refreshing

# Player 1 Event Listeners
screen.onkeypress(wPressed, "w")
screen.onkeyrelease(wReleased, "w")
screen.onkeypress(aPressed, "a")
screen.onkeyrelease(aReleased, "a")
screen.onkeypress(dPressed, "d")
screen.onkeyrelease(dReleased, "d")
screen.onkeypress(spacePressed, "space")
screen.onkeyrelease(spaceReleased, "space")
 
# Player 2 Event Listeners
screen.onkeypress(upArrowPressed, "Up")
screen.onkeyrelease(upArrowReleased, "Up")
screen.onkeypress(leftArrowPressed, "Left")
screen.onkeyrelease(leftArrowReleased, "Left")
screen.onkeypress(rightArrowPressed, "Right")
screen.onkeyrelease(rightArrowReleased, "Right")
screen.onclick(mouseClicked)

screen.listen()
 
gameloop()
    
