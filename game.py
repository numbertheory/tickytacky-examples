from tickytacky.scene import Scene
from tickytacky.run_app import RunApp


main_screen = Scene(title="game",
                    fixed=True,
                    height=160,
                    width=240,
                    sprites=["snail_sprite.json", "tile_sprite.json"])


if __name__ == "__main__":
    main_screen.window.sprites["floor1"]["location"] = [20, 20]
    main_screen.window.sprites["snail"]["location"] = [100, 20]
    main_screen.window.draw_all_sprites(["snail", "floor1"])
    RunApp().run()
