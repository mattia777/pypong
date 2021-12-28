# https://www.youtube.com/watch?v=XGf2GcyHPhc



import turtle                                       # turtle is a module\library that enalbles to create graphics as pictures and shapes
import winsound

# window
window = turtle.Screen()                            # create a window
window.title('Pong by @mattia')                     # window title
window.bgcolor('black')                             # background window color
window.setup(width=800, height=600)                 # dimension window, (0, 0) is the center
window.tracer(0)                                    # stops the update of the window so that we have to update it manually, it speeds up the code

# score players
score_a = 0
score_b = 0

# score default text
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write('Player 1: 0 - Player 2: 0 ', align= 'center', font=('Courier', 16, 'normal'))

# paddle A
paddle_a = turtle.Turtle()                          # Turtle object
paddle_a.speed()                                    # sets the speed of the animation to max
paddle_a.shape('square')                            # sets the shape of the paddle to a square, 20pixel x 20pixel
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    # streches the with by 20x5 and the len is 20x1
paddle_a.color('red')                               # sets the color to red
paddle_a.penup()                                    #
paddle_a.goto(-350, 0)                              # sets the paddle position to the coordinates (-350,0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed() 
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('blue')
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed()
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

ball.dx = 0.6                                       # ball moves by 0.6 pixels, x axis
ball.dy = 0.6                                       # ball moves by 0.6  pixels, y axis

# functions
def paddle_a_up():
    y = paddle_a.ycor()                             # assigning to y the y coord
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()                             # assigning to y the y coord
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

#keyboard binding
window.listen()                                     # listens for a keaborad input

window.onkeypress(paddle_a_up, 'w')                 # if the user presses 'w' it calls the function paddle_a_up
window.onkeypress(paddle_a_down, 's')

window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')


# every game needs a Main game loop
while True:
    window.update()                                 # every time the loop runs it updates the screen
    

    # move the ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy)

    # border check TOP
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1                               # reverse the derection of the ball
        winsound.PlaySound('beat.wav', winsound.SND_ASYNC)
    
    # border check BOTTOM
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        winsound.PlaySound('beat.wav', winsound.SND_ASYNC)
        
    # border check SCORE PLAYER 1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= -1 
        score_a += 1
        score.clear()
        score.write('Player 1: {} - Player 2: {} '.format(score_a,score_b), align= 'center', font=('Courier', 16, 'normal'))
        winsound.PlaySound('harmony.wav', winsound.SND_ASYNC)
        
    # border check SCORE PLAYER 2
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1 
        score_b += 1
        score.clear()
        score.write('Player 1: {} - Player 2: {} '.format(score_a,score_b), align= 'center', font=('Courier', 16, 'normal'))
        winsound.PlaySound('harmony.wav', winsound.SND_ASYNC)
        
        
    
# paddle and ball collision 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +45 and ball.ycor() > paddle_b.ycor() -45):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound('player2.wav', winsound.SND_ASYNC)
        

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +45 and ball.ycor() > paddle_a.ycor() -45):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound('player1.wav', winsound.SND_ASYNC)
        

