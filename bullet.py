import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, hero_x, hero_y, screen_size):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()  # наследуем свойства у родителя Sprite
        self.width_screen = screen_size[0]  # сохраням для дальнейшей работы ширину экрана
        self.height_screen = screen_size[1]  # высоту экрана
        self.image = pygame.Surface((15, 45))  # создаём фигуру
        self.image.fill(color=(0, 255, 0))  # зарисовываем фигуру в цвет
        self.rect = self.image.get_rect()  # создаём хтбокс персонажа
        self.rect.centerx = hero_x # расположение по x
        self.rect.centery = hero_y # расположение по y
        self.speedx = 0
        self.speedy = -5

    def update(self):
        if self.rect.centery < 0: # убиваем , если вылитела за верхнию границу экрана
            self.kill()
        self.rect.centery += self.speedy


