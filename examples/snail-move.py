import pyglet
from tickytacky.screen import Screen
from tickytacky.sprite import Sprite

sprites = Sprite(["snail_sprite.json"])
main_screen = Screen(title="game",
                     fixed=True,
                     pixel_sprites=sprites.pixel_sprites)


def init():
    main_screen.add_sprite("snail", [10, 10])


def update(dt):
    old_loc = main_screen.sprites["snail"]["location"]
    new_loc = [old_loc[0] + 1, old_loc[1]]
    main_screen.add_sprite("snail", new_loc)
    pass


if __name__ == "__main__":
    # Start it up!
    init()

    pyglet.clock.schedule_interval(update, 1/12)

    pyglet.app.run()
