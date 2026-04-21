class Ball:
    def __init__(self, x, y, radius=25, speed=20, screen_size=(1200, 700)):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.screen_width, self.screen_height = screen_size


    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= self.screen_width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= self.screen_height - self.radius:
            self.y = new_y

    def draw(self, screen, pygame):
        pygame.draw.circle(screen, (127, 0, 255), (self.x, self.y), self.radius)