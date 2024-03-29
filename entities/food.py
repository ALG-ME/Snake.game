import pygame

class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.TITLE_SIZE
        self.rect = pygame.rect.Rect([0, 0, game.TITLE_SIZE - 2, game.TITLE_SIZE - 2])
        self.rect.center = self.game.snake.get_random_pos()

    def draw(self):
        pygame.draw.rect(self.game.screen, 'red', self.rect)