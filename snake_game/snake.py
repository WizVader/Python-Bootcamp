import turtle

NEW_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Running a for loop to create new segments of our snake in the new positions.
    1) Choosing the shape of our segment
    2) Choosing colour of segment
    3) Pen up to send the segments to their respective positions without the animation being displayed on screen
    4) Adding segments into a list to keep track
    """

    def __init__(self):
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]
    def create_segments(self):
        for positions in NEW_POSITIONS:
            self.add_segment(positions)

    def move(self):
        """
        To make sure that the segments look like they are attached and in one piece,
         we are sending each segment to the previous segments location (Starting from the last).
         So this way, all the pieces will be attached to each other and will follow each others path
        """
        for i in range(len(self.segments) - 1, 0, -1):
            x_coordinate = self.segments[i - 1].xcor()
            y_coordinate = self.segments[i - 1].ycor()
            self.segments[i].goto(x_coordinate, y_coordinate)

        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, positions):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_segments()
        self.head = self.segments[0]
