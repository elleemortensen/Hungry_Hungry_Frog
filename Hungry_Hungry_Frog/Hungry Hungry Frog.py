import arcade
import random

SPRITE_SCALING_PLAYER = 0.7
SPRITE_SCALING_FLY = 0.25
FLY_COUNT = 100
MOVEMENT_SPEED = 5

SCREEN_WIDTH = 775
SCREEN_HEIGHT = 600

class Leaderboard(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.SEA_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("LEADERBOARD ", SCREEN_WIDTH / 2, 450,
                         arcade.color.BLACK, font_size=35, anchor_x="center")
        arcade.draw_text("Number of times won in a row: ", SCREEN_WIDTH / 2, 400,
                         arcade.color.SMOKY_BLACK, font_size=25, anchor_x="center")
        arcade.draw_text("1. Ellee - 8 ", SCREEN_WIDTH / 2, 350,
                         arcade.color.SMOKY_BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("2. Holly - 6 ", SCREEN_WIDTH / 2, 300,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("3. Payton - 2 ", SCREEN_WIDTH / 2, 250,
                         arcade.color.SMOKY_BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("4. Kate - 1 " , SCREEN_WIDTH / 2, 200,
                         arcade.color.SMOKY_BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = InstructionView()
        game_view.on_show_view()
        self.window.show_view(game_view)

class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.SEA_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Help the frog catch all the flies. ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=35, anchor_x="center")
        arcade.draw_text("Avoid getting stung by the bees! ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.BLACK, font_size=35, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.SMOKY_BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Game()
        game_view.setup()
        self.window.show_view(game_view)

class Bee_3(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.hit_sound = arcade.load_sound("upgrade4.wav")
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1.215
            arcade.play_sound(self.hit_sound)

        elif self.bottom <= 0 or self.top >= SCREEN_HEIGHT:
            self.change_y *= -1.215
            arcade.play_sound(self.hit_sound)

        self.center_x += self.change_x
        super(Bee_3, self).update()

class Bee_2(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.hit_sound = arcade.load_sound("upgrade4.wav")
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1.215
            arcade.play_sound(self.hit_sound)

        elif self.bottom <= 0 or self.top >= SCREEN_HEIGHT:
            self.change_y *= -1.215
            arcade.play_sound(self.hit_sound)

        self.center_x += self.change_x
        super(Bee_2, self).update()

class Bee(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.hit_sound = arcade.load_sound("upgrade4.wav")
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1.215
            arcade.play_sound(self.hit_sound)

        elif self.bottom <= 0 or self.top >= SCREEN_HEIGHT:
            self.change_y *= -1.215
            arcade.play_sound(self.hit_sound)

        self.center_x += self.change_x
        super(Bee, self).update()

class Frog(arcade.Sprite):
    def update(self):
        if self.left <= 0:
            self.center_x = 45
        elif self.right >= SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH - 45
        elif self.bottom <= 0:
            self.center_y = 50
        elif self.top >= SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT - 5

        super(Frog, self).update()

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.window.set_mouse_visible(False)
        self.eating_sound = arcade.load_sound("coin5.wav")
        arcade.set_background_color(arcade.color.SEA_BLUE)

    def setup(self):
        self.all_sprites_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()
        self.bee_list = arcade.SpriteList()
        self.bee_2_list = arcade.SpriteList()
        self.bee_3_list = arcade.SpriteList()
        self.frog_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = Frog("frog.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)
        self.bee = Bee("bee.png", .5)
        self.fly = arcade.Sprite("fly.png", SPRITE_SCALING_FLY)
        self.bee.center_x = random.randrange(100, 675)
        self.bee.center_y = random.randrange(100, 500)
        self.bee_list.append(self.bee)
        self.all_sprites_list.append(self.bee)
        self.bee.change_x = 1
        self.bee.change_y = 1

        self.bee_2 = Bee_2("bee.png", .5)
        self.bee_2.center_x = random.randrange(100, 675)
        self.bee_2.center_y = random.randrange(100, 500)
        self.bee_2_list.append(self.bee_2)
        self.all_sprites_list.append(self.bee_2)
        self.bee_2.change_x = 1
        self.bee_2.change_y = 1

        self.bee_3 = Bee_3("bee.png", .5)
        self.bee_3.center_x = random.randrange(100, 675)
        self.bee_3.center_y = random.randrange(100, 500)
        self.bee_3_list.append(self.bee_3)
        self.all_sprites_list.append(self.bee_3)
        self.bee_3.change_x = 1
        self.bee_3.change_y = 1

        for number in range(FLY_COUNT):
            fly = arcade.Sprite("fly.png", SPRITE_SCALING_FLY)
            fly.center_x = random.randrange(SCREEN_WIDTH - 20)
            fly.center_y = random.randrange(SCREEN_HEIGHT - 20)
            self.all_sprites_list.append(fly)
            self.fly_list.append(fly)
            self.fly.change_x = 1
            self.fly.change_y = 1

    def on_draw(self):
        arcade.start_render()
        # lily pads
        arcade.draw_circle_filled(300, 280, 50, arcade.color.SPANISH_GREEN)
        arcade.draw_triangle_filled(300, 280, 250, 265, 250, 295, arcade.color.SEA_BLUE)
        arcade.draw_circle_filled(450, 430, 50, arcade.color.SPANISH_GREEN)
        arcade.draw_triangle_filled(450, 430, 500, 445, 500, 415, arcade.color.SEA_BLUE)
        arcade.draw_circle_filled(550, 175, 45, arcade.color.SPANISH_GREEN)
        arcade.draw_triangle_filled(550, 175, 550, 235, 595, 210, arcade.color.SEA_BLUE)
        arcade.draw_circle_filled(115, 115, 55, arcade.color.SPANISH_GREEN)
        arcade.draw_triangle_filled(115, 115, 115, 50, 55, 85, arcade.color.SEA_BLUE)
        arcade.draw_circle_filled(180, 475, 40, arcade.color.SPANISH_GREEN)
        arcade.draw_triangle_filled(160, 430, 200, 430, 180, 475, arcade.color.SEA_BLUE)
        # flowers
        arcade.draw_circle_filled(77, 390, 10, arcade.color.LAVENDER_PURPLE)
        arcade.draw_circle_filled(65, 400, 10, arcade.color.LAVENDER_PURPLE)
        arcade.draw_circle_filled(53, 390, 10, arcade.color.LAVENDER_PURPLE)
        arcade.draw_circle_filled(57, 376, 10, arcade.color.LAVENDER_PURPLE)
        arcade.draw_circle_filled(73, 376, 10, arcade.color.LAVENDER_PURPLE)
        arcade.draw_circle_filled(65, 387, 9, arcade.color.PINK_LAVENDER)

        arcade.draw_circle_filled(700, 105, 10, arcade.color.GOLDEN_YELLOW)
        arcade.draw_circle_filled(688, 115, 10, arcade.color.GOLDEN_YELLOW)
        arcade.draw_circle_filled(676, 105, 10, arcade.color.GOLDEN_YELLOW)
        arcade.draw_circle_filled(680, 91, 10, arcade.color.GOLDEN_YELLOW)
        arcade.draw_circle_filled(696, 91, 10, arcade.color.GOLDEN_YELLOW)
        arcade.draw_circle_filled(688, 102, 9, arcade.color.LIGHT_RED_OCHRE)

        arcade.draw_circle_filled(335, 237, 10, arcade.color.BABY_BLUE)
        arcade.draw_circle_filled(323, 247, 10, arcade.color.BABY_BLUE)
        arcade.draw_circle_filled(311, 237, 10, arcade.color.BABY_BLUE)
        arcade.draw_circle_filled(316, 223, 10, arcade.color.BABY_BLUE)
        arcade.draw_circle_filled(332, 223, 10, arcade.color.BABY_BLUE)
        arcade.draw_circle_filled(323, 234, 9, arcade.color.LAVENDER_PURPLE)

        arcade.draw_circle_filled(525, 302, 10, arcade.color.PINK_LAVENDER)
        arcade.draw_circle_filled(513, 312, 10, arcade.color.PINK_LAVENDER)
        arcade.draw_circle_filled(501, 302, 10, arcade.color.PINK_LAVENDER)
        arcade.draw_circle_filled(506, 288, 10, arcade.color.PINK_LAVENDER)
        arcade.draw_circle_filled(522, 288, 10, arcade.color.PINK_LAVENDER)
        arcade.draw_circle_filled(513, 299, 9, arcade.color.WHITE)

        arcade.draw_circle_filled(206, 65, 10, arcade.color.LIGHT_RED_OCHRE)
        arcade.draw_circle_filled(194, 75, 10, arcade.color.LIGHT_RED_OCHRE)
        arcade.draw_circle_filled(182, 65, 10, arcade.color.LIGHT_RED_OCHRE)
        arcade.draw_circle_filled(186, 51, 10, arcade.color.LIGHT_RED_OCHRE)
        arcade.draw_circle_filled(202, 51, 10, arcade.color.LIGHT_RED_OCHRE)
        arcade.draw_circle_filled(194, 62, 9, arcade.color.BABY_BLUE)

        arcade.draw_circle_filled(665, 490, 10, arcade.color.PASTEL_MAGENTA)
        arcade.draw_circle_filled(653, 500, 10, arcade.color.PASTEL_MAGENTA)
        arcade.draw_circle_filled(641, 490, 10, arcade.color.PASTEL_MAGENTA)
        arcade.draw_circle_filled(645, 476, 10, arcade.color.PASTEL_MAGENTA)
        arcade.draw_circle_filled(661, 476, 10, arcade.color.PASTEL_MAGENTA)
        arcade.draw_circle_filled(653, 487, 9, arcade.color.GOLDEN_YELLOW)

        arcade.draw_circle_filled(266, 515, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(254, 525, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(242, 515, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(246, 501, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(262, 501, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(254, 512, 9, arcade.color.PASTEL_MAGENTA)

        self.all_sprites_list.draw()
        output = f"Flies Eaten: {self.score}"
        arcade.draw_text(output, 650, 575, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.ESCAPE:
            arcade.exit()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        self.all_sprites_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.fly_list)

        for fly in hit_list:
            fly.kill()
            self.score += 1
            arcade.play_sound(self.eating_sound)
            if self.score > 99:
                game_view = WinView()
                self.window.show_view(game_view)

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.bee_list)

        for fly in hit_list:
            game_view = EndView()
            self.window.show_view(game_view)

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.bee_2_list)

        for fly in hit_list:
            game_view = EndView()
            self.window.show_view(game_view)

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.bee_3_list)

        for fly in hit_list:
            game_view = EndView()
            self.window.show_view(game_view)

class WinView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.SEA_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("WINNER WINNER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("FLY DINNER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to play again", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Game()
        game_view.setup()
        self.window.show_view(game_view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()

class EndView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.SEA_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("GAME", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("OVER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to play again", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Game()
        game_view.setup()
        self.window.show_view(game_view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Hungry Hungry Frog")
    leaderboard_view = Leaderboard()
    window.show_view(leaderboard_view)
    arcade.run()

if __name__ == "__main__":
    main()


