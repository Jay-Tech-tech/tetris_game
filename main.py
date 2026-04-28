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
    if sprite.is_touching_edge() and sprite == ( and False):
        storage.put_number(StorageSlots.S1, 0)
basic.forever(on_forever)
