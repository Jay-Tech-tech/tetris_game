input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    sprite.change(LedSpriteProperty.X, -1)
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    sprite.change(LedSpriteProperty.X, 1)
})
let sprite: game.LedSprite = null
let list: number[] = []
let X = 0
let Y = 0
let spielfeld = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
sprite = game.createSprite(2, 0)
loops.everyInterval(1000, function () {
    sprite.change(LedSpriteProperty.Y, 1)
})
basic.forever(function () {
    X = sprite.get(LedSpriteProperty.X)
    Y = sprite.get(LedSpriteProperty.Y)
    if (Y == 4) {
        spielfeld[Y][X] = 1
        game.createSprite(X, Y)
sprite.set(LedSpriteProperty.Y, 0)
        sprite.set(LedSpriteProperty.X, 2)
    } else if (spielfeld[Y + 1][X] == 1) {
        spielfeld[Y][X] = 1
        game.createSprite(X, Y)
sprite.set(LedSpriteProperty.Y, 0)
        sprite.set(LedSpriteProperty.X, 2)
    }
})
