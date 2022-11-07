# arcade platformer
# Martin Goff

import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale sprites from original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels/frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# player starting position
PLAYER_START_X = 64
PLAYER_START_Y = 225

# layer names from TileMap
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_DONT_TOUCH = "Don't Touch"


class MyGame(arcade.Window):
    '''
    Main application class
    '''

    def __init__(self):

        # call parent class and set up window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # TileMap Object
        self.tile_map = None

        # scene object
        self.scene = None

        # separate variable that holds player sprite
        self.player_sprite = None

        # physics engine
        self.physics_engine = None

        # camera used to scroll the screen
        self.camera = None

        # camera used to draw GUI elements
        self.gui_camera = None

        # keep track of score
        self.score = 0

        # should score be reset
        self.reset_score = True

        # where is right edge of map
        self.end_of_map = 0

        # level
        self.level = 1

        # load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")

    def setup(self):
        """Set up game here. Call this function to reset game."""

        # set up cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # map name
        map_name = f":resources:tiled_maps/map2_level_{self.level}.json"

        # layer specific options for the TileMap
        layer_options = {
            LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_COINS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_DONT_TOUCH: {
                "use_spatial_hash": True,
            },
        }

        # load in TileMap
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # initialize scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # keep track of score, make sure score kept if player finishes level
        if self.reset_score:
            self.score = 0
        self.reset_score = True

        # add player spritelist before foreground layer. this makes foreground
        # be drawn after player, making it appear to be in front of player.
        # setting before using scene.add_sprite allows us to define where spritelist
        # will be in draw order. if just use add_sprite, will be appended to
        # end of order
        self.scene.add_sprite_list_after("Player", self.player_sprite)

        # set up player at specific coordinates
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite("Player", self.player_sprite)

        # --- Load in map from tiled editor ---

        # calculate right edge of my_map in pixels
        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        # --- other stuff
        # set background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # create physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, 
            gravity_constant=GRAVITY, 
            walls=self.scene[LAYER_NAME_PLATFORMS]
        )

    def on_draw(self):
        """Render the screen."""

        # clear the screen to the background color
        self.clear()

        # activate game camera
        self.camera.use()

        # draw scene
        self.scene.draw()

        # activate GUI camera before drawing GUI elements
        self.gui_camera.use()

        # draw score on screen, scrolling it w/ viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.WHITE,
            18
        )

    def on_key_press(self, key, modifiers):
        """called when a certain key is pressed"""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """called when user releases key"""

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
        """movement and game logic"""

        # move player with physics engine
        self.physics_engine.update()

        # see if any coins are hit
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Coins"]
        )

        # loop through each coin hit (if any) and remove it
        for coin in coin_hit_list:
            # remove coin
            coin.remove_from_sprite_lists()
            # play a sound
            arcade.play_sound(self.collect_coin_sound)
            # add one to score
            self.score += 1

        # did player fall off map?
        if self.player_sprite.center_y < -100:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            arcade.play_sound(self.game_over)

        # did player touch something they should not?
        if arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_DONT_TOUCH]
        ):
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            arcade.play_sound(self.game_over)

        # position camera
        self.center_camera_to_player()


def main():
    """main function"""
    window = MyGame()
    window.setup()
    arcade.run()

# means we can import this program and use functions from this program in other programs
if __name__ == "__main__":
    main()