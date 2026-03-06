from turtle import *


class Sprite(Turtle):
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True 
        else:
            return False

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))
    
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)
    
player = Sprite(0, -100, 10, 'circle', 'orange')
goal = Sprite(10, 200, 0,'triangle', 'green')
red1 = Sprite(-200, 100, 15, 'square', 'red')
red1.set_move(-200, 100, 200, 100)
red2 = Sprite(200, 15, 15, 'square', 'red')
red2.set_move(200, 15, -200, 15)
scr = player.getscreen()
scr.listen()


scr.onkey(player.move_up, 'w')
scr.onkey(player.move_left, 'a')
scr.onkey(player.move_right, 'd')
scr.onkey(player.move_down, 's')

total_score = 0

while total_score < 3:
    red1.make_step()
    red2.make_step()
    if player.is_collide(goal):
        player.goto(0, -100)
        total_score += 1
    if player.is_collide(red1) or player.is_collide(red2):
        goal.hideturtle()
        break

red1.hideturtle()
red2.hideturtle()
if total_score >= 3:
    win = Turtle()
    win.write('winner', font=('Arial', 20, 'bold'))
    win.hideturtle()
elif total_score < 3:
    lose = Turtle()
    lose.write('Lose', font=('Arial', 20, 'bold'))
    lose.hideturtle()
