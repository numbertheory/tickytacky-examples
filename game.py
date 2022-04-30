from pyglet.window import key
from tickytacky.screen import Screen
from tickytacky.sprite import Sprite
from tickytacky.clock import Clock
from tickytacky.run_app import RunApp

sprites = Sprite(["snail_sprite.json"])
main_screen = Screen(title="game",
                     fixed=True,
                     height=160,
                     width=240,
                     pixel_sprites=sprites.pixel_sprites)
main_screen.set_fullscreen(True)


def init():
    main_screen.add_sprite("snail", [10, 10])


def snail(new_loc=False):
    old_loc = main_screen.sprites["snail"]["location"]
    if new_loc:
        move_snail = [old_loc[0] + new_loc[0], old_loc[1] + new_loc[1]]
        main_screen.add_sprite("snail", move_snail)
    else:
        main_screen.add_sprite("snail", old_loc)


def update(dt):
    snail()
    pass


def up():
    snail([0, -1])


def down():
    snail([0, 1])


def left():
    snail([-1, 0])


def right():
    snail([1, 0])


@main_screen.event
def on_text_motion(motion):
    arrow_keys = {
        key.MOTION_UP: up,
        key.MOTION_DOWN: down,
        key.MOTION_LEFT: left,
        key.MOTION_RIGHT: right
    }
    arrow_keys[motion]()


if __name__ == "__main__":
    # Start it up!
    init()
    Clock().schedule_interval(update, 1/12)
    RunApp().run()
