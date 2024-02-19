from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

'''
Starting with the setup of the screen.
1) Calling the screen class
2) Setting up the height and width
3) Choosing the bg colour and title
4) Turning off the animation updates for our graphics window
'''
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

new_positions = [(0, 0), (-20, 0), (-40, 0)]  # Creating a list of, starting positions for the snake

segments = []  # Empty list to add our turtle segments

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:

    screen.update()  # Updating our screen only after we have performed actions for all three segments
    time.sleep(0.08)  # Creating a time delay to see the snake move properly
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
