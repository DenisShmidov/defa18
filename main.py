import pygame
import hero

pygame.init()  # подгружаем все зависимости в ручную
pygame.mixer.init() # подгрузка звуковой логики

shot_sound = pygame.mixer.Sound('sound/выстрел.MP3') # добовляем звуки
reload_sound = pygame.mixer.Sound('sound/reload.MP3')
pygame.mixer.music.load('sound/Billie_Eilish_-_Ocean_Eyes_47841905.mp3') # музыка бегкраунда
pygame.mixer.music.set_volume(0.1)
shot_sound.set_volume(0.2) # уменьшаем громкость
reload_sound.set_volume(0.2)

clock = pygame.time.Clock()  # создание таймера
FPS = 60

BLACK_RED = (99, 82, 82)

screen_size = wight, height = 900, 900
screen = pygame.display.set_mode(screen_size)  # создание игрового экрана

all_sprites = pygame.sprite.Group()
all_hero = pygame.sprite.Group()
all_bullet = pygame.sprite.Group()
for i in range(-wight, wight + 1, wight):
    hero_main = hero.Player(screen_size, wight // 2 + i, height // 2)
    all_sprites.add(hero_main)
    all_hero.add(hero_main)

shooting_time = 0
shooting_delay = 15 # количество игровых тиков перед выстрелом
shooting_run = False # если труе персонаж стреляет


magazine_capacity = 10 # маккс кол потрон
magazine = magazine_capacity # сколько потронов сейчас
magazine_reload = 0
magazine_delay = 60

pygame.mixer.music.play()
music_play = True
run = True
while run:
    clock.tick(FPS)  # сколько игровой цикл повторяеться в секунду
    screen.fill(BLACK_RED)  # Зарисовка всего экрана в цвет

    # стрельба
    if shooting_run == True:
        shooting_time += 1 # создаём задержку перед выстрилами
        if shooting_time >= shooting_delay and magazine >= 1: #
            for hero in all_hero: # перебираем всех героев
                shot_sound.play() # издать звук выстрела
                bullet = hero.shoting()
                all_bullet.add(bullet)
                all_sprites.add(bullet)
            shooting_time = 0
            magazine -= 1

        if magazine <= 0: # отвечает за перезарядку
            if magazine_reload == 0:
                    reload_sound.play()
            magazine_reload += 1
            if magazine_reload >= magazine_delay:
                magazine = magazine_capacity
                magazine_reload = 0

    for event in pygame.event.get():  # обработчик всех событий в игре
        if event.type == pygame.QUIT:  # обработка события выход
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # по нажатию кнопки включаем выключаем музыку
                music_play = not music_play
                if music_play:
                    pygame.mixer.music.unpause()
                if not music_play:
                    pygame.mixer.music.pause()
            if event.key == pygame.K_SPACE:
                shooting_run = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shooting_run = False

    all_sprites.update()  # запускаем метод update всех спрайтой внутри all_sprites
    all_sprites.draw(screen)  # отрисовываем объекты

    pygame.display.update()  # обновление экрана

pygame.quit()
