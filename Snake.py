import threading
import time


class Position(object):
    """
    It represents a coordinate in Cartesian System
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Slice:
    """
    It represents the part of the snake body
    """
    def __init__(self, position: Position):
        self.position = position

    def __repr__(self):
        return "(" + str(self.position.x) + ", " + str(self.position.y) + ")"


class Snake:
    def __init__(self):
        self.length = 0
        self.slices = [Slice(Position(10, 13)),
                       Slice(Position(10, 12)),
                       Slice(Position(10, 11)),
                       Slice(Position(10, 10))]
        self.direction = "forward"

    def get_delta_x_and_delta_y(self):
        delta_x = 0
        delta_y = 0

        if self.direction == "forward":
            delta_y = 1
        elif self.direction == "backward":
            delta_y = -1
        elif self.direction == "left":
            delta_x = -1
        elif self.direction == "right":
            delta_x = 1

        return delta_x, delta_y

    def move_one_step_forward(self):
        """assuming snake is moving forward"""
        print(self.slices)
        delta_x, delta_y = self.get_delta_x_and_delta_y()
        last_slice = self.slices.pop()
        first_slice = self.slices[0]
        new_slice = Slice(Position(first_slice.position.x + delta_x, first_slice.position.y + delta_y))
        self.slices.insert(0, new_slice)

    def set_direction(self, direction, reverse_allowed=False):
        if direction not in ["forward", "backward", "left", "right"]:
            raise Exception("direction can only be: forward", "backward", "left", "right")

        if not reverse_allowed:
            if (self.direction == "forward" and direction == "backward") or \
                    (self.direction == "backward" and direction == "forward") or \
                    (self.direction == "left" and direction == "right") or \
                    (self.direction == "right" and direction == "left"):
                raise Exception("Snake cant reverse")

        print("setting direction as ", direction)
        self.direction = direction


def run_snake(s):
    for i in range(20):
        s.move_one_step_forward()
        time.sleep(1)


s = Snake()
thread = threading.Thread(target=run_snake, args=(s,))
thread.start()

