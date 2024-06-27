from turtle import *
from collections import deque
import turtle

def min_of_list(numbers):
    return min(numbers)

def min_of_stack(stack):
    min_stack = float('inf')
    while min_stack:
        min_stack = min(min_stack, min_stack.pop())
    return min_stack
    
def min_of_queue(queue):
    min_queue = float('inf')
    while min_queue:
        min_queue = min(min_queue, min_queue.popleft())
    return min_queue

def draw_circle_and_text(text, x, y, radius, font_size=16, align="center"):
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.fillcolor("yellow")  # Set fill color to blue
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

    # Write text after drawing the circle (avoids overwriting)
    pen.penup()
    pen.goto(x, y - radius // 3)  # Adjust y position for text placement
    pen.pendown()
    pen.write(text, align="center", font=("Arial", font_size, "normal"))

def main():
    X = float(input("Enter the first number (X): "))
    Y = float(input("Enter the second number (Y): "))
    Z = float(input("Enter the third number (Z): "))
    numbers = [X, Y, Z]

    min_list = min_of_list(numbers)
    stack = numbers[:]
    min_stack = min_of_stack(stack)
    queue = deque(numbers)
    min_queue = min_of_queue(queue)

    # Set up the turtle window
    turtle.setup(width=500, height=400)  # Adjust window size as needed
    turtle.hideturtle()
    
    # Draw circle and write text
    draw_circle_and_text(f"Minimum Value: {min_list}", 0, 0, 100)

    turtle.done()

if __name__ == "__main__":
    main()
