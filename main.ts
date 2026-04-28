input.onButtonEvent(Button.A, input.buttonEventClick(), function on_button_a() {
    sprite.change(LedSpriteProperty.X, -1)
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function on_button_b() {
    sprite.change(LedSpriteProperty.X, 1)
})
let sprite : game.LedSprite = null
sprite = game.createSprite(2, 0)
loops.everyInterval(1000, function on_every_interval() {
    sprite.change(LedSpriteProperty.Y, 1)
})
basic.forever(function on_forever() {
    if (sprite.isTouchingEdge() && sprite == (sprite && false)) {
        storage.putNumber(StorageSlots.s1, 0)
    }
    
})
