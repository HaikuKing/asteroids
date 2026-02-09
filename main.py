import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def draw_score(surface, score_value, font):
    score_text = font.render(f"Score: {score_value}", True, "white")
    surface.blit(score_text, (10, 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids - as made by HaikuKing")
    font = pygame.font.Font(None, 36)
    score = 0

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)

        for rock in asteroids:
            for bullet in shots:
                if rock.collision(bullet) == True:
                    bullet.kill()
                    rock.split()
                    score += 50
            if rock.collision(player) == True:
                print(f"\nGame over!\nYour Final Score: {score}")
                sys.exit()

        for object in drawable:
            object.draw(screen)

        draw_score(screen, score, font)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
