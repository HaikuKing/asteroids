from circleshape import *
from constants import *


class Player(CircleShape): # type: ignore
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) # type: ignore
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # type: ignore

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt # type: ignore

    def update(self, dt):
        keys = pygame.key.get_pressed() # type: ignore

        if keys[pygame.K_a]: # type: ignore
            self.rotate(dt * (-1))
        if keys[pygame.K_d]: # type: ignore
            self.rotate(dt)
        if keys[pygame.K_w]: # type: ignore
            self.move(dt)
        if keys[pygame.K_s]: # type: ignore
            self.move(dt * (-1))

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        self.position += forward * PLAYER_SPEED * dt # type: ignore