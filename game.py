import pygame as pg

# Test
pg.init()
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
finished = False

square_is_teal = True
teal_color = (42, 222, 222)
red_color = (222, 42, 42)
x_pos = 375
y_pos = 275
movement_speed = 4
clock = pg.time.Clock()

# Game loop
while not finished:
    # Process events
    movement_delta = {"x": 0, "y": 0}
    speed_delta = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                square_is_teal = not square_is_teal
            if event.key == pg.K_KP_PLUS:
                speed_delta += 1
            if event.key == pg.K_KP_MINUS:
                speed_delta -= 1

    # Update speed
    if speed_delta != 0:
        movement_speed += speed_delta
        if movement_speed < 0:
            movement_speed = 0

    # Get position input
    pressed_keys = pg.key.get_pressed()
    if pressed_keys[pg.K_UP]:
        movement_delta['y'] -= movement_speed
    if pressed_keys[pg.K_DOWN]:
        movement_delta['y'] += movement_speed
    if pressed_keys[pg.K_LEFT]:
        movement_delta['x'] -= movement_speed
    if pressed_keys[pg.K_RIGHT]:
        movement_delta['x'] += movement_speed

    # Update position
    updated_x_pos = x_pos + movement_delta['x']
    if 0 <= updated_x_pos <= screen_width:
        x_pos = updated_x_pos

    updated_y_pos = y_pos + movement_delta['y']
    if 0 <= updated_y_pos <= screen_width:
        y_pos = updated_y_pos

    # Drawing test
    screen.fill((0, 0, 0))
    square_color = teal_color if square_is_teal else red_color
    pg.draw.rect(screen, square_color, pg.Rect(x_pos, y_pos, 50, 50))

    # Swap display buffers (there are two)
    pg.display.flip()
    clock.tick(60)
