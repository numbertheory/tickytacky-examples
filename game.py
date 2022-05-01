from tickytacky.scene import Scene
from tickytacky.run_app import RunApp


main_screen = Scene(title="game",
                    fixed=True,
                    height=160,
                    width=240,
                    sprites=["snail_sprite.json", "tile_sprite.json"])


if __name__ == "__main__":
    print(main_screen.sprites)
    main_screen.sprites["snail"]["location"] = [10, 10]
    main_screen.sprites["floor1"]["location"] = [20, 20]
    RunApp().run()
