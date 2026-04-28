def on_button_a():
    sprite.change(LedSpriteProperty.X, -1)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    sprite.change(LedSpriteProperty.X, 1)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

sprite: game.LedSprite = None
sprite = game.create_sprite(2, 0)

def on_every_interval():
    sprite.change(LedSpriteProperty.Y, 1)
loops.every_interval(1000, on_every_interval)

def on_forever():
    # Prüft, ob der Punkt ganz unten angekommen ist (Y-Koordinate ist 4)
    if sprite.get(LedSpriteProperty.Y) == 4:
        storage.put_number(StorageSlots.S1, 0)
basic.forever(on_forever)
