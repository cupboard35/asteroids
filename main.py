import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shots import *


def main():
	pygame.init()
	updatable = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
 
	AsteroidField.containers = (updatable)
	Asteroid.containers = (asteroids, updatable, drawables)
	Player.containers = (updatable, drawables)
	Shot.containers = (shots, updatable, drawables)
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0
	clock = pygame.time.Clock()
	asteroid_field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

 
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)
  
		for asteroid in asteroids:
			if asteroid.collision_detection(player):
				print(f"Game Over!")
				sys.exit()
    
			for shot in shots:
				if shot.collision_detection(asteroid):
					shot.kill()
					asteroid.split()


		pygame.Surface.fill(screen, "black")
  
		for drawable in drawables:
			drawable.draw(screen)
   
		pygame.display.flip()
		dt = (clock.tick(60))/1000

if __name__ == "__main__":
	main()
