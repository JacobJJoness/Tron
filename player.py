class Player:
    def __init__(self, start_x, start_y, color):
        self.x = start_x
        self.y = start_y
        self.color = color
        self.direction = "RIGHT"

    def move(self):
        if self.direction == "UP":
            if self.y > 0:  # Check if player is not at the top edge
                self.y -= .5
        elif self.direction == "DOWN":
            if self.y < 1490:  # Check if player is not at the bottom edge
                self.y += .5
        elif self.direction == "LEFT":
            if self.x > 0:  # Check if player is not at the left edge
                self.x -= .5
        elif self.direction == "RIGHT":
            if self.x < 1990:  # Check if player is not at the right edge
                self.x += .5
    
    def change_direction(self, new_direction):
        if (self.direction == "UP" and new_direction != "DOWN") or \
        (self.direction == "DOWN" and new_direction != "UP") or \
        (self.direction == "LEFT" and new_direction != "RIGHT") or \
        (self.direction == "RIGHT" and new_direction != "LEFT"):
            self.direction = new_direction