import pygame
import heapq

# Ayarlar
TILE_SIZE = 24
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Farklı haritalar (her level için)
maps = [
    [  # Level 1
        "##############",
        "#............#",
        "#.###.#####..#",
        "#.###.#####..#",
        "#.....###....#",
        "#.###.###.##.#",
        "#.###.###..#.#",
        "#............#",
        "##############"
    ],
    [   #Level 2
        "####################",
        "#..................#",
        "#.###..#.##.####.#.#",
        "#..................#",
        "#.##..#######.#.##.#",
        "#.##..#######.#.##.#",
        "#..................#",
        "####################"

    ],
    [  # Level 3
        "#####################",
        "#......##......##...#",
        "#.####.##.####.##.#.#",
        "#.................#.#",
        "#.##.########.#.##.##",
        "#........##.........#",
        "#####################"
    ],
    [  # Level 4
        "############################",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#..........................#",
        "#.##.##########.##########.#",
        "#..........................#",
        "#.##.##.#########.##.##.##.#",
        "#......##........##......#.#",
        "######.####.##.####.######.#",
        "#............##............#",
        "############################"
    ]
]

# A* Fonksiyonu
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal, game_map):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)

        x, y = current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            next_pos = (nx, ny)
            if 0 <= ny < len(game_map) and 0 <= nx < len(game_map[0]):
                if game_map[ny][nx] != "#" and next_pos not in visited:
                    new_cost = cost + 1
                    priority = new_cost + heuristic(next_pos, goal)
                    heapq.heappush(open_set, (priority, new_cost, next_pos, path + [next_pos]))
    return [start]

# Başlat
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pac-Man AI - Level Sistemi")
clock = pygame.time.Clock()

# Başlangıç değerleri
level = 1
score = 0
game_speed = 10

# Harita yükleyici
def load_level(lvl):
    global game_map, ROWS, COLS, WIDTH, HEIGHT, pacman_x, pacman_y, ghosts, dots
    game_map = maps[min(lvl - 1, len(maps) - 1)]
    ROWS = len(game_map)
    COLS = len(game_map[0])
    WIDTH = COLS * TILE_SIZE
    HEIGHT = ROWS * TILE_SIZE
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pacman_x, pacman_y = 1, 1
    ghosts = [(COLS - 2, ROWS - 2) for _ in range(lvl)]
    dots = set()
    for row in range(ROWS):
        for col in range(COLS):
            if game_map[row][col] == ".":
                dots.add((col, row))

load_level(level)
frame_counter = 0
running = True

# Game over ekranı
def game_over_screen():
    waiting = True
    while waiting:
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 30)
        msg = font.render("Kaybettin! İyi denemeydi.", True, (200, 0, 0))
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//20))
        btn_font = pygame.font.SysFont(None, 36)
        btn1 = pygame.Rect(WIDTH//2 - 100, HEIGHT//3, 200, 50)
        btn2 = pygame.Rect(WIDTH//2 - 100, HEIGHT//3 + 70, 200, 50)
        pygame.draw.rect(screen, (0, 200, 0), btn1)
        pygame.draw.rect(screen, (200, 0, 0), btn2)
        text1 = btn_font.render("Tekrar Oyna", True, (255, 255, 255))
        text2 = btn_font.render("Çık", True, (255, 255, 255))
        screen.blit(text1, (btn1.x + 40, btn1.y + 10))
        screen.blit(text2, (btn2.x + 80, btn2.y + 10))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn1.collidepoint(event.pos):
                    return
                elif btn2.collidepoint(event.pos):
                    pygame.quit()
                    exit()

# Oyun döngüsü
while running:
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            tile = game_map[row][col]
            if tile == "#":
                pygame.draw.rect(screen, BLUE, (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile == "." and (col, row) in dots:
                pygame.draw.circle(screen, (200, 200, 200), (col*TILE_SIZE + TILE_SIZE//2, row*TILE_SIZE + TILE_SIZE//2), 3)

    # Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x*TILE_SIZE + TILE_SIZE//2, pacman_y*TILE_SIZE + TILE_SIZE//2), TILE_SIZE//2 - 2)

    # Hayaletler
    for gx, gy in ghosts:
        pygame.draw.circle(screen, RED, (gx*TILE_SIZE + TILE_SIZE//2, gy*TILE_SIZE + TILE_SIZE//2), TILE_SIZE//2 - 2)

    # Seviye ve skor
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Seviye: {level}  Skor: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]: dx = -1
    if keys[pygame.K_RIGHT]: dx = 1
    if keys[pygame.K_UP]: dy = -1
    if keys[pygame.K_DOWN]: dy = 1

    new_x = pacman_x + dx
    new_y = pacman_y + dy
    if 0 <= new_x < COLS and 0 <= new_y < ROWS and game_map[new_y][new_x] != "#":
        pacman_x, pacman_y = new_x, new_y

    # Nokta yeme
    if (pacman_x, pacman_y) in dots:
        dots.remove((pacman_x, pacman_y))
        score += 10
        if not dots:
            level += 1
            game_speed += 1
            load_level(level)

    # Hayalet hareketi
    frame_counter += 1
    if frame_counter % 5 == 0:
        new_ghosts = []
        for gx, gy in ghosts:
            path = astar((gx, gy), (pacman_x, pacman_y), game_map)
            if len(path) > 1:
                next_step = path[1]
                new_ghosts.append(next_step)
            else:
                new_ghosts.append((gx, gy))
        ghosts = new_ghosts

    # Çarpışma
    for gx, gy in ghosts:
        if gx == pacman_x and gy == pacman_y:
            game_over_screen()
            level = 1
            score = 0
            game_speed = 10
            load_level(level)

    clock.tick(game_speed)

pygame.quit()
