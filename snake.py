from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_length = 3
        self.snake_sections = []
        self.create_snake()
        self.head = self.snake_sections[0]

    def create_snake(self, ):
        for snakes_pos in STARTING_POSITIONS:
            self.add_segment(snakes_pos)

    def add_segment(self,snakes_pos):
        sections = Turtle("square")
        sections.color("red")
        sections.penup()
        sections.setpos(snakes_pos)
        self.snake_sections.append(sections)

    def extend(self):
        self.add_segment(self.snake_sections[-1].position())
        self.snake_length += 1

    def move(self):
        for part_num in range(len(self.snake_sections)- 1, 0, -1):
            new_x = self.snake_sections[part_num - 1].xcor()
            new_y = self.snake_sections[part_num - 1].ycor()
            self.snake_sections[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)

    def reset(self):
        for seg in self.snake_sections:
            seg.goto(1000, 1000)
        self.snake_sections.clear()
        self.create_snake()
        self.head = self.snake_sections[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
