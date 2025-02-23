import pygame
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    hp = 10

    def __init__(self, screen_size, x, y):  # запускаеться при создание экземпляра класса
        super().__init__()  # наследуем свойства init родителя
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.images = []
        for i in range(1, 5):
            self.images.append(pygame.transform.scale(pygame.image.load(f"image/right{i}.png"),
                                                      (150, 150)))  # загрузка и уменьшение картинки
        self.image = self.images[3]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 5
        self.m = 0
        self.number_images = 0

    def update(self):
        self.m += 1
        if self.m >= 12:
            print(0)
            self.number_images += 1
            if self.number_images >= 4:
                self.number_images = 0
            self.m = 0
            self.image = self.images[self.number_images]
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.rect.centerx -= self.speed
        if key[pygame.K_d]:
            self.rect.centerx += self.speed
        if key[pygame.K_z]:
            self.speed += 1  # ускорение здесь
        if key[pygame.K_w]:
            self.rect.centery -= self.speed
        if key[pygame.K_s]:
            self.rect.centery += self.speed

        if self.rect.right < 0 - self.width:
            self.rect.right = self.width + self.width

        if self.rect.left > self.width + self.width:
            self.rect.left = 0 - self.width

        # self.rect.top -верх self.rect.right - правая граница персожанал self.rect.left - левая часть персонажа
        if self.rect.bottom > self.height:  # если нижния граница персонада > высоты экрана
            self.rect.bottom = self.height

        if self.rect.top < 0:  # если верхняя граница < 0
            self.rect.top = 0

    def shoting(self):

        bullet = Bullet(self.rect.centerx, self.rect.centery, (self.width, self.height))
        return bullet
