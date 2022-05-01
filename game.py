from pyglet.window import key
from tickytacky.scene import Scene
from tickytacky.clock import Clock
from tickytacky.run_app import RunApp


main_screen = Scene(title="game",
                    fixed=True,
                    height=160,
                    width=240,
                    sprites=["snail_sprite.json", "tile_sprite.json"])
# main_screen.set_fullscreen(True)


def init():
    main_screen.window.add_sprite("snail", [10, 10])
    main_screen.window.add_sprite("floor1", [30, 30])


def snail(new_loc=False):
    old_loc = main_screen.pixel_sprites["snail"].get("location")
    if new_loc:
        move_snail = [old_loc[0] + new_loc[0], old_loc[1] + new_loc[1]]
        main_screen.window.add_sprite("snail", move_snail)
    else:
        main_screen.window.add_sprite("snail", old_loc)


def update(dt):
    main_screen.update_scene()
    snail()


def up():
    snail([0, -1])


def down():
    snail([0, 1])


def left():
    snail([-1, 0])


def right():
    snail([1, 0])


@main_screen.window.event
def on_text_motion(motion):
    snail()
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
    Clock().schedule_interval(update, 1/36)
    RunApp().run()
