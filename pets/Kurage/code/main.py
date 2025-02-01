import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time

display = PyGameDisplay(width=128, height=128, flags=pygame.OPENGL)
splash = displayio.Group()
display.show(splash)

assets = {
    "background": displayio.OnDiskBitmap("Assets/Background.bmp"),
    "bubble": displayio.OnDiskBitmap("Assets/Bubble.bmp"),
    "bubble_column": displayio.OnDiskBitmap("Assets/Bubble Column.bmp"),
    "bubbles": displayio.OnDiskBitmap("Assets/Bubbles.bmp"),
    "food": displayio.OnDiskBitmap("Assets/Food.bmp"),
    "kurage": displayio.OnDiskBitmap("Assets/Kurage.bmp"),
}


bg_sprite = displayio.TileGrid(
    assets["background"],
    pixel_shader=assets["background"].pixel_shader
)
splash.append(bg_sprite)

kurage_sprite = displayio.TileGrid(
    assets["kurage"],
    pixel_shader=assets["kurage"].pixel_shader,
    width=1,
    height=1,
    tile_width=64,
    tile_height=64,
    default_tile=0,
    x= display.width // 2 - 32,
    y= display.height // 2 - 32,
)

splash.append(kurage_sprite)

frame = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            pass

    # kurage_sprite. = frame
    # frame = (frame + 1) % (cat_sheet.width // tile_width)

    keys = pygame.key.get_pressed()
    time.sleep(0.1)
#
#    if game_over == False:
#        if keys[pygame.K_LEFT]:
#            cat_sprite.x -= speed
#        if keys[pygame.K_RIGHT]:
#            cat_sprite.x += speed
#        if random.random() < 0.05:  # spawn rate
#            spawn_fireball()
#
#    for fireball in fireballs:
#        fireball.y += 5
#        if fireball.y > display.height:
#            splash.remove(fireball)
#            fireballs.remove(fireball)
#        elif check_collision(cat_sprite, fireball):
#            game_over = True
#            display_game_over()
#
#
#