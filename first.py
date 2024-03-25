import os
import sys
import pygame
import pygame_gui
import random

pygame.init()

# Основные настройки
size = width, height = 880, 660
screen = pygame.display.set_mode(size)
screen.fill((76, 75, 80))
pygame.display.set_caption("Погоняй-ка!")
TILE_SIZE = 30
FPS = 50
manager = pygame_gui.UIManager((width, height))
orientation = 'NESW'

clock = pygame.time.Clock()

# функция загрузки изображения из папки data
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# Функция выхода из игры  Надо дописать переспрос
def terminate():
    pygame.quit()
    sys.exit()

# Функция с мини-циклом по загрузке стартового окна
def start_screen():
    intro_text = ["Игра-стратегия 'ПОГОНЯЙ-КА!' для 1, 2 или 3 участников",
                  "Правила игры: игрок 'кидает' кубик, выпавшее количество ходов расходует на",
                  "повороты, разгон, торможение и перемещение по полю", "Нажмите Enter чтобы начать игру"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (880, 481))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 24)
    text_coord = 490
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # переход к следующему окну
        pygame.display.flip()
        clock.tick(FPS)

# Функция с мини-циклом вывода окна правил
def rule_screen():
    intro_text = ["Правила игры 'ПОГОНЯЙ-КА!'", "",
                  "Игрок 'бросает' 2 кубика (получает от 2 до 12 очков)",
                  "Начальная скорость - 0 км/ч. Для набора скорости на 50 км/ч тратится 1 очко",
                  "(переключение на 1 передачу) и так до 3 скорости - 150 км/ч максимальная",
                  "скорость. На одной клетке можно увеличить скорость на одну передачу.",
                  "1 очко тратится на снижение скорости на 50 км/ч - аналогично разгону.",
                  "1 очко тратится для поворота на клетке, если скорость 1. ",
                  "На 2 и 3 передаче повернуть нельзя.",
                  "Для перемещения на 1 клетку вперед тратится на 1 скорости - 3 очка",
                  "на 2-й скорости - 2 очка, на 3-й скорости - 1 очко.",
                  "Цена действий на клетках вне трассы удваивается.",
                  "При шаге в клетку, где находится соперник, игра завершается вашим проигрышем.",
                  "Необходимо добраться от линии старта до линии финиша.",
                  "Для управления используйте кнопки на панели приборов.",
                  "Читайте подсказки, они помогут :))"]

# формирование окна с кнопкой
    rule_window = pygame.Surface((800, 450))
    rule_window.fill((76, 75, 80))
    font = pygame.font.Font(None, 50)
    textOK = font.render('OK', 1, (250, 250, 250))
    pygame.draw.rect(rule_window, 'grey', (750, 400, 50, 50), 0)
    rule_window.blit(textOK, (752, 412))
    screen.blit(rule_window, (10, 10))

# Заготовка для текста
    font = pygame.font.Font(None, 22)
    text_coord = 25
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 15
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] in range(760,811) and event.pos[1] in range(410, 461):
                    return  # переход к следующему окну
        pygame.display.flip()
        clock.tick(FPS)

# Функция с мини-циклом вывода окна результатов
def result_screen(intro_text):
    # формирование окна с кнопкой
    result_window = pygame.Surface((400, 450))
    result_window.fill((78, 78, 78))
    font = pygame.font.Font(None, 50)
    textOK = font.render('OK', 1, (250, 250, 250))
    pygame.draw.rect(result_window, 'grey', (350, 400, 50, 50), 0)
    result_window.blit(textOK, (352, 412))
    screen.blit(result_window, (10, 10))

    # Заготовка для текста
    font = pygame.font.Font(None, 24)
    text_coord = 25
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 15
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] in range(360, 410) and event.pos[1] in range(410, 461):
                    return  # переход к следующему окну
        pygame.display.flip()
        clock.tick(FPS)
#запуск стартового окна
start_screen()
#запуск окна с правилами
rule_screen()


# Функция загрузки карты уровня
def load_level(filename):
    filename = "maps\\" + filename
    map_ = []
    with open(filename, 'r') as karta:
        for line in karta:
            map_.append(list(map(int, line.split())))
    return map_

# Функция расчета стоимости действия на игровом поле
def is_enough(ball, flag, v, pl, land_gr):
    if pygame.sprite.spritecollideany(pl, land_gr):
        shtraf = 2
    else:
        shtraf = 1
    if flag != 'f':
        ball = ball * shtraf
    else:
        if v == 1:
            ball = 3 * shtraf
        elif v == 2:
            ball = 2 * shtraf
        elif v == 3:
            ball = 1 * shtraf
    return ball

# Словари иллюстраций для спрайтов поля и героев
tile_images = {
    'land': pygame.transform.scale(load_image('grass.png'), (TILE_SIZE, TILE_SIZE)),
    'track': pygame.transform.scale(load_image('trass.png'), (TILE_SIZE, TILE_SIZE)),
    'start': pygame.transform.scale(load_image('start.png'), (TILE_SIZE, TILE_SIZE)),
    'finish': pygame.transform.scale(load_image('finish.png'), (TILE_SIZE, TILE_SIZE))}

player_images = {
    '0_N': pygame.transform.scale(load_image('car_r.png', -1), (TILE_SIZE, TILE_SIZE)),
    '0_S': pygame.transform.scale(load_image('car_r_d.png', -1), (TILE_SIZE, TILE_SIZE)),
    '0_W': pygame.transform.scale(load_image('car_r_l.png', -1), (TILE_SIZE, TILE_SIZE)),
    '0_E': pygame.transform.scale(load_image('car_r_r.png', -1), (TILE_SIZE, TILE_SIZE)),
    '1_N': pygame.transform.scale(load_image('car_g.png', -1), (TILE_SIZE, TILE_SIZE)),
    '1_S': pygame.transform.scale(load_image('car_g_d.png', -1), (TILE_SIZE, TILE_SIZE)),
    '1_W': pygame.transform.scale(load_image('car_g_l.png', -1), (TILE_SIZE, TILE_SIZE)),
    '1_E': pygame.transform.scale(load_image('car_g_r.png', -1), (TILE_SIZE, TILE_SIZE)),
    '2_N': pygame.transform.scale(load_image('car_b.png', -1), (TILE_SIZE, TILE_SIZE)),
    '2_S': pygame.transform.scale(load_image('car_b_d.png', -1), (TILE_SIZE, TILE_SIZE)),
    '2_W': pygame.transform.scale(load_image('car_b_l.png', -1), (TILE_SIZE, TILE_SIZE)),
    '2_E': pygame.transform.scale(load_image('car_b_r.png', -1), (TILE_SIZE, TILE_SIZE))}


# Класс клетки поля
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(TILE_SIZE * pos_x, TILE_SIZE * pos_y)
# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_images['0_N'] # передать тип игрока
        self.rect = self.image.get_rect().move(TILE_SIZE * pos_x, TILE_SIZE * pos_y) #проверить размер
        self.orientation = 0

    def rotate(self, direction):
        if direction >= 0:
            self.image = player_images[f'0_{orientation[direction % 4]}'] # передать тип игрока
        else:
            self.image = player_images[f'0_{orientation[direction + abs(direction) // 4 * 4 ]}']

    def update(self, dx, dy):
        self.rect.x += dx * TILE_SIZE
        self.rect.y += dy * TILE_SIZE
# группы спрайтов
all_sprites = pygame.sprite.Group()
land_group = pygame.sprite.Group()
finish_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
# Функция создания игрового поля и игрока
def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 1:
                Tile('track', x, y)
            elif level[y][x] == 2:
                Tile('land', x, y)
                land_group.add(Tile('land', x, y))
            elif level[y][x] == 4:
                Tile('finish', x, y)
                finish_group.add(Tile('finish', x, y))
            elif level[y][x] == 3:
                Tile('start', x, y)
            elif level[y][x] == 8:
                Tile('start', x, y)
                new_player = Player(x, y)
    return new_player
# Функция по расчету сдвига в зависимости от поворота игрока
def delta(n):
    if n <= 0:
        n = n + abs(n) // 4 * 4
    else:
        n = n % 4
    if orientation[n] == 'N':
        delx = 0
        dely = -1
    elif orientation[n] == 'E':
        delx = 1
        dely = 0
    elif orientation[n] == 'S':
        delx = 0
        dely = 1
    elif orientation[n] == 'W':
        delx = -1
        dely = 0
    return delx, dely
# Прорисовка панели управления
panel = pygame.Surface((300, 660))
panel.fill(pygame.Color((146, 188, 214)))
sp_gamer = pygame.font.Font(None, 24)
for i in range(3):
    label_gamer = sp_gamer.render(f'Игрок {i + 1}', 1, (78, 78, 78))
    panel.blit(label_gamer, (25, 20 + 50 * i  ))
# Рисуем кнопки
turn_right = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((800, 350), (79, 50)),
    text='Направо',
    manager=manager)
turn_left = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((602, 350), (79, 50)),
    text='Налево',
    manager=manager)
boost_transmission = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((700, 320), (96, 50)),
    text='Быстрее',
    manager=manager)
lower_transmission = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((700, 380), (96, 50)),
    text='Медленнее',
    manager=manager)
forward = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((700, 450), (96, 50)),
    text='ВПЕРЕД!',
    manager=manager)
dice = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((760, 550), (96, 50)),
    text= 'Бросаем',
    manager=manager)
trassa_1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((650, 160), (96, 50)),
    text='Трасса 1',
    manager=manager)
trassa_2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((750, 160), (96, 50)),
    text= 'Трасса 2',
    manager=manager)
ch_level = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((700, 220), (96, 50)),
    text= 'Выбрать',
    manager=manager)
stop_game = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((750, 620), (96, 35)),
    text= 'Выход',
    manager=manager)
rule = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((620, 620), (96, 35)),
    text= 'Правила',
    manager=manager)
# Рисуем поля ввода имени игрока (про запас на будущее)
entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((720, 15), (100, 35)), manager=manager, object_id='1')
entry1 = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((720, 65), (100, 35)), manager=manager, object_id='2')
entry2 = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((720, 115), (100, 35)), manager=manager, object_id='3')
# Функция действия на игровом поле
def choice_level(level):
    del_x = 0
    del_y = -1
    direct = 0
    count = 0
    speed = 0
    bros = 0
    fl = 'n'
    flag = ''
    t = ''
    first = second = 0
    name = 'Не определен'
    sum_count = 0

    player = generate_level(load_level(f'location_{level}.txt'))

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        if event.ui_element == entry:
                            name = event.text
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == stop_game:
                        terminate()
                    if event.ui_element == rule:
                        rule_screen()
                    if event.ui_element == dice:
                        bros += 1
                        first = random.randint(1,6)
                        second = random.randint(1,6)
                        count = first + second
                        t = ''
                    if event.ui_element == turn_left:
                        flag = 'l'
                        if speed > 1:
                            text = font.render(f'На скорости {speed} поворачивать нельзя. Снижайте скорость', 1,
                                               (255, 255, 255))
                            t = '1'
                        else:
                            price = is_enough(1, flag, speed, player, land_group)
                            if price > count:
                                text = font.render(f'Цена действия {price} очков. Осталось очков: {count}. '
                                                   f'Кидайте кубики', 1, (255, 255, 255))
                                t = '1'
                            else:
                                direct -= 1
                                player.rotate(direct)
                                del_x, del_y = delta(direct)
                                count -= price
                                sum_count += price
                                t = ''
                    if event.ui_element == turn_right:
                        flag = 'r'
                        if speed > 1:
                            text = font.render(f'На скорости {speed} поворачивать нельзя. Снижайте скорость', 1, (255, 255, 255))
                            t = '1'
                        else:
                            price = is_enough(1, flag, speed,  player, land_group)
                            if price > count:
                                text = font.render(f'Цена действия {price} очков. Осталось очков: {count}. '
                                                   f'Кидайте кубики', 1, (255, 255, 255))
                                t = '1'
                            else:
                                direct += 1
                                count -= price
                                sum_count += price
                                player.rotate(direct)
                                del_x, del_y = delta(direct)
                                t = ''
                    if event.ui_element == boost_transmission:
                        flag = 'up'
                        if speed == 3:
                            text = font.render(f'Скорость больше 3 не предусмотрена', 1, (255, 255, 255))
                            t = '1'
                        else:
                            if flag == fl:
                                text = font.render(f'Повторный разгон в одной клетке стоит дороже', 1, (255, 255, 255))
                                t = '1'
                                price = is_enough(2, flag, speed, player, land_group)
                            else:
                                price = is_enough(1, flag, speed, player, land_group)
                            if price > count:
                                text = font.render(f'Цена действия {price} очков. Осталось очков: {count}. '
                                                   f'Кидайте кубики', 1, (255, 255, 255))
                                t = '1'
                            else:
                                count -= price
                                sum_count += price
                                speed += 1
                                t = ''
                    if event.ui_element == lower_transmission:
                        flag = 'down'
                        if speed == 0:
                            text = font.render(f'Отрицательная скорость не предусмотрена', 1, (255, 255, 255))
                            t = '1'
                        else:
                            if flag == fl:
                                font = pygame.font.Font(None, 24)
                                text = font.render(f'Повторное торможение в одной клетке стоит дороже', 1, (255, 255, 255))
                                screen.blit(text, (25, 620))
                                pygame.time.delay(3000)
                                price = is_enough(2, flag, speed, player, land_group)
                            else:
                                price = is_enough(1, flag, speed, player, land_group)
                            if price > count:
                                text = font.render(f'Цена действия {price} очков. Осталось очков: {count}. '
                                                   f'Кидайте кубики', 1, (255, 255, 255))
                                t = '1'
                            else:
                                count -= price
                                sum_count += price
                                speed -= 1
                                t = ''
                    if event.ui_element == forward:
                        flag = 'f'
                        if speed == 0:
                            text = font.render(f' Наберите скорость. На скорости 0 ехать невозможно', 1, (255, 255, 255))
                            t = '1'
                        else:
                            price = is_enough(0, flag, speed, player, land_group)
                            if price > count:
                                text = font.render(f'Цена действия {price} очков. Осталось очков: {count}. '
                                                   f'Кидайте кубики', 1, (255, 255, 255))
                                t = '1'
                            else:
                                count -= price
                                sum_count += price
                                t = ''
                                if (0 <= player.rect.x + del_x <= 600 - TILE_SIZE and
                                    0 <= player.rect.y + del_y <= 600 - TILE_SIZE):
                                    player.update(del_x, del_y)
                                else:
                                    text = font.render(f'Выезд за пределы карты запрещен', 1, (255, 255, 255))
                                    t = '1'
                    # del_x, del_y = delta(direct)
            manager.process_events(event)
        manager.update(time_delta)
        if flag:
            fl = flag
        screen.fill((76,75, 80))
        tiles_group.draw(screen)
        player_group.draw(screen)
        kubiki = pygame.transform.scale(pygame.image.load('data\\kub.jpg'), (128, 60))
        panel.blit(kubiki, (20, 550))
        kub_first = pygame.transform.scale(pygame.image.load(f'data\\kub_{first}.png'), (50, 50))
        panel.blit(kub_first, (162, 500))
        kub_second = pygame.transform.scale(pygame.image.load(f'data\\kub_{second}.png'), (50, 50))
        panel.blit(kub_second, (222, 500))
        screen.blit(panel, (600, 0))
        manager.draw_ui(screen)
        font = pygame.font.Font(None, 24)
        if not t:
            text = font.render(f'Игрок: {name}, скорость: {speed}, осталось очков: {count}', 1, (255, 255, 255))
        else:
            pygame.time.delay(1000)
        screen.blit(text, (25, 620))
        pygame.display.update()
        if pygame.sprite.spritecollideany(player, finish_group):
            screen.fill((146, 188, 214))
            font = pygame.font.Font(None, 24)
            text = font.render(f'Гонка завершена! Ваш результат {sum_count} очков, сделано {bros} бросков',
                               1, (78, 78, 78))
            screen.blit(text, (25, 620))
            pygame.time.delay(3000)
            with open("data\\records.txt", 'r', encoding="utf8") as output_file:
                inf = []
                for line in output_file:
                    inf.append(line.strip().split('\t'))
                if len(inf[-1]) == 0:
                   a = inf.pop()
                inf.append([str(choice_lev), name, str(sum_count), str(bros)])
            inf = [inf[0]] + sorted(inf[1:], key=lambda x: int(x[2]))
            inf_result = [' '.join(x) for x in inf[:6]]
            result_screen(inf_result)
            with open('data\\records.txt', 'w', encoding="utf8") as f:
                for x in inf[:6]:
                    print('\t'.join(x), file=f)
            all_sprites.empty()
            player_group.empty()
            tiles_group.empty()
            finish_group.empty()
            land_group.empty()
            return
        clock.tick(FPS)
    return
# Основной игровой цикл, в котором можно выбрать игровое поле
choice_lev = 0
tt = ''
run = True
while run:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == stop_game:
                    terminate()
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == trassa_1:
                    choice_lev = 1
                    tt = '1'
                    text = font.render(f'Выбрана трасса 1. Подтвердите выбор кнопкой "Выбрать"', 1,
                                       (255, 255, 255))
                if event.ui_element == trassa_2:
                    choice_lev = 2
                    tt = '1'
                    text = font.render(f'Выбрана трасса 2. Подтвердите выбор кнопкой "Выбрать"', 1,
                                       (255, 255, 255))
                if event.ui_element == ch_level:
                    if choice_lev:
                        choice_level(choice_lev)
                    else:
                        tt = '1'
                        text = font.render(f'Сначала выберите трассу. Подтвердите выбор кнопкой "Выбрать"', 1,
                                           (255, 255, 255))
        manager.process_events(event)
    manager.update(time_delta)
    screen.fill((76,75, 80))
    kubiki = pygame.transform.scale(pygame.image.load('data\\kub.jpg'), (128, 60))
    panel.blit(kubiki, (20, 550))
    screen.blit(panel, (600, 0))
    manager.draw_ui(screen)
    font = pygame.font.Font(None, 24)
    if not tt:
        text = font.render(f'Выберите трассу. Подтвердите выбор кнопкой "Выбрать"', 1, (255, 255, 255))
    else:
        pygame.time.delay(500)
    screen.blit(text, (25, 620))
    pygame.display.update()
    clock.tick(FPS)
terminate()