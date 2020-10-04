import turtle
import playsound

# window for the settings
# sn = turtle.Screen()
# sn.title("Pong")
# sn.bgcolor("black")
# sn.setup(width=800, height=600)
# sn.tracer(0)

# prompting colors for the game and winning score
maximal_score = int(input("Enter the winning score for this game: "))
game_bg_color = str(input("Enter a color for the background of the game: "))
paddle_color = str(input("Enter a color for the paddles: "))
ball_color = str(input("Enter a color for the ball: "))

# window for the game
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor(game_bg_color)
wn.setup(width=800, height=600)
wn.tracer(0)


# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color(paddle_color)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color(paddle_color)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color(ball_color)
ball.penup()
ball.goto(0, 0)
ball.dx = .25
ball.dy = .25


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {0} Player B: {1}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * (-1)
        playsound.playsound("Pongsound.mp3", False)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * (-1)
        playsound.playsound("Pongsound.mp3", False)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * (-1)

        # keeping score
        score_a = score_a + 1

        pen.clear()
        pen.write("Player A: {0} Player B: {1}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * (-1)

        # keeping score
        score_b = score_b + 1

        pen.clear()
        pen.write("Player A: {0} Player B: {1}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if 330 < ball.xcor() < 350 and paddle_b.ycor() - 40 < ball.ycor() < paddle_b.ycor() + 40:
        ball.dx = ball.dx * (-1)

    if -350 < ball.xcor() < -330 and paddle_a.ycor() - 40 < ball.ycor() < paddle_a.ycor() + 40:
        ball.dx = ball.dx * (-1)

    # Prevent Paddles from moving off the board
    if paddle_a.ycor() > 260:
        paddle_a.sety(260)

    if paddle_a.ycor() < -260:
        paddle_a.sety(-260)

    if paddle_b.ycor() > 260:
        paddle_b.sety(260)

    if paddle_b.ycor() < -260:
        paddle_b.sety(-260)

    # Check if someone has won by gettin the winning score
    if score_a == maximal_score:
        print("Player A won the game.")
        break
    elif score_b == maximal_score:
        print("Player B won the game.")
        break
