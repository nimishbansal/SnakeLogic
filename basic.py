# Python program to draw square
# using Turtle Programming
import turtle

INITIAL_DIRECTION = "up"

direction = INITIAL_DIRECTION

skk = turtle.Turtle()
stack = [(50, 50)]
STEP_SIZE = 1


def move_one_step_in_specified_direction(direction_param, stack_param):
    global STEP_SIZE
    if direction_param == "up":
        stack_param.push((stack_param[-1][0], stack_param[-1][1] + STEP_SIZE))
    elif direction_param == "down":
        stack_param.push((stack_param[-1][0], stack_param[-1][1] - STEP_SIZE))
    elif direction_param == "left":
        stack_param.push((stack_param[-1][0] - STEP_SIZE, stack_param[-1][1]))
    elif direction_param == "right":
        stack_param.push((stack_param[-1][0] + STEP_SIZE, stack_param[-1][1]))


while True:
    move_one_step_in_specified_direction(direction, stack)

# turtle.done()
