import pygame
import sys

from config import *


class GameField(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], width, height, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((width, height))
        self.image.fill('#1e1e1e')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        pass


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()

        self.running = True

        self.all_sprites = pygame.sprite.Group()

        self.game_field = GameField((30, 30), 350, 590, self.all_sprites)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill('#0f1c3f')

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()