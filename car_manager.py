from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.create_cars()

    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.resizemode('user')
        new_car.shapesize(1, 2)





# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#
#     def car_position(self, ):
#
#     def make_car(self):
#         for color in COLORS:
#             self.shape('square')
#             self.resizemode('user')
#             self.shapesize(1, 2)
#             self.color(color)
#
