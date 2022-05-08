from pyglet.window import key
from tickytacky.scene import Scene
from tickytacky.clock import Clock
from tickytacky.run_app import RunApp

main_screen = Scene(title="game",
                    fixed=True,
                    height=160,
                    width=240,
                    sprites=["snail_sprite.json"],
                    tile_files=["tile_inv.json", "tile_obv.json"],
                    scene_data="scene_data.json")


def init():
    main_screen.window.sprites["snail"]["location"] = [100, 20]
    main_screen.window.draw_all_sprites(["snail"])
    main_screen.load_scene("scene1")
    main_screen.window.text(text="Press C to change scenery.",
                            font_directory="fonts/",
                            font="VCR OSD Mono",
                            position=[100, 100])


def snail(new_loc=False):
    old_loc = main_screen.window.sprites["snail"].get("location")
    if new_loc:
        move_snail = [old_loc[0] + new_loc[0], old_loc[1] + new_loc[1]]
        main_screen.window.add_sprite("snail", move_snail)
    else:
        main_screen.window.add_sprite("snail", old_loc)


def update(dt):
    main_screen.window.draw_all_sprites(["snail"])


def up():
    snail([0, -1])


def down():
    snail([0, 1])


def left():
    snail([-1, 0])


def right():
    snail([1, 0])


@main_screen.window.event
def on_key_press(symbol, modifiers):
    key_binds = {
        key.C: switch_scene
    }
    try:
        key_binds[symbol]()
    except KeyError:
        # not all motion keys are mapped
        pass


def switch_scene():
    if not main_screen.current_scene:
        main_screen.current_scene = "scene1"
    if main_screen.current_scene == "scene1":
        main_screen.load_scene("scene2")
    elif main_screen.current_scene == "scene2":
        main_screen.load_scene("scene1")


@main_screen.window.event
def on_text_motion(motion):
    arrow_keys = {
        key.MOTION_UP: up,
        key.MOTION_DOWN: down,
        key.MOTION_LEFT: left,
        key.MOTION_RIGHT: right,
    }
    try:
        arrow_keys[motion]()
    except KeyError:
        # not all motion keys are mapped
        pass


@main_screen.window.event
def on_draw():
    main_screen.window.draw_all_sprites(["snail"])


if __name__ == "__main__":
    # Start it up!
    init()
    Clock().schedule_interval(update, 1/36)
    RunApp().run()
