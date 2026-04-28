input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    sprite.change(LedSpriteProperty.X, -1)
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    sprite.change(LedSpriteProperty.X, 1)
})
let sprite: game.LedSprite = null
let list: number[] = []
let spielfeld = [1, 2, 3]
sprite = game.createSprite(2, 0)
loops.everyInterval(1000, function () {
    sprite.change(LedSpriteProperty.Y, 1)
})
basic.forever(function () {
	if (Y == 4){}

    if ((spielfeld [Y + 1][X] == 1)){;}
    
})
