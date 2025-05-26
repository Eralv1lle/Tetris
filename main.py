import pygame
import sys

from config import *


class GameField(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], width, height, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((width, height))
        self.image.fill('#521761')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        pass


class Block:
    def __init__(self, type_block):
        self.type_block = type_block
        self.x = square_size * 6
        self.y = square_size * 6
        self.rects = blocks[self.type_block]


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()

        self.running = True

        self.all_sprites = pygame.sprite.Group()

        self.game_field = GameField((30, 30), 300, 600, self.all_sprites)
        self.grid = [[pygame.Rect(col * square_size, row * square_size, square_size, square_size) for col in range(1, width_square_size + 1)] for row in range(1, height_square_size + 1)]

        self.i_block = Block('I')

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill('#ba3dd9')

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            for i in self.i_block.rects:
                pygame.draw.rect(self.screen, (0, 0, 0), i, border_radius=3)

            for squares in self.grid:
                for square in squares:
                    pygame.draw.rect(self.screen, '#ba3dd9', square, 1)


            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()