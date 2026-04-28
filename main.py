def on_button_a():
    sprite.change(LedSpriteProperty.X, -1)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    sprite.change(LedSpriteProperty.X, 1)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

sprite: game.LedSprite = None
list2: List[number] = []
X = 0
Y = 0
spielfeld = [[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
sprite = game.create_sprite(2, 0)

def on_every_interval():
    sprite.change(LedSpriteProperty.Y, 1)
loops.every_interval(1000, on_every_interval)

def on_forever():
    global X, Y
    X = sprite.get(LedSpriteProperty.X)
    Y = sprite.get(LedSpriteProperty.Y)
    if Y == 4:
        spielfeld[Y][X] = 1
        game.create_sprite(X, Y)
        sprite.set(LedSpriteProperty.Y, 0)
        sprite.set(LedSpriteProperty.X, 2)
    elif spielfeld[Y + 1][X] == 1:
        spielfeld[Y][X] = 1
        game.create_sprite(X, Y)
        sprite.set(LedSpriteProperty.Y, 0)
        sprite.set(LedSpriteProperty.X, 2)
basic.forever(on_forever)
