# arcade platformer
# Martin Goff

import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants for sprites
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

# Movement speed of player, pixels/frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        

        self.scene = None

        self.player_sprite = None

        self.physics_engine = None

        self.camera = None

        self.gui_camera = None

        self.score = 0

        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):

        self.camera = arcade.Camera(self.width, self.height)

        self.gui_camera = arcade.Camera(self.width, self.height)

        self.score = 0

        self.scene = arcade.Scene()

        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        # set up player at specific coordinates
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        # creates ground
        for x in range (0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        # put crates on ground
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # add crate on ground
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
            )
            wall.position = coordinate
            self.scene.add_sprite("Walls", wall)

        for x in range(128, 1250, 256):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)
            coin.center_x = x
            coin.center_y = 96
            self.scene.add_sprite("Coins", coin)

        # create physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Walls"]
        )

    def on_draw(self):
        self.clear()

        self.camera.use()

        self.scene.draw()

        self.gui_camera.use()

        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.WHITE,
            18
        )

    def on_key_press(self, key, modifiers):

        # called when a certain key is pressed
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        # called when user releases key
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )

        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):

        # moves player with physics engine
        self.physics_engine.update()

        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Coins"]
        )

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 1

        # position camera
        self.center_camera_to_player()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

# means we can import this program and use functions from this program in other programs
if __name__ == "__main__":
    main()