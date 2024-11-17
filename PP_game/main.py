import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong Game'

class Bal(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.1)
        self.change_x = 3.7
        self.change_y = 3.7

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.4)

    def update(self):
        self.center_x += self.change_x
        if self.right >=SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0




class Game(arcade.Window):

    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title)
        self.bar = Bar()
        self.ball = Bal()
        self.setup()

    def setup(self):

        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_WIDTH / 8
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_WIDTH / 4

    def on_draw(self):
        self.clear((200, 200, 200))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar,self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 7
        if key == arcade.key.LEFT:
            self.bar.change_x = -7

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or  key == arcade.key.LEFT:
            self.bar.change_x = 0




if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
