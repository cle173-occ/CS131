from arcade.gui import*

import os

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Calculator"
Value = ""

class num0(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="0"):
        super().__init__(x, y, width, height, text)
        self.game = game
        
    def on_press(self):
        self.pressed = True
        global Value
        Value += "0"
    def on_release(self):
        self.pressed = False
        print(Value)
class num1(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="1", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "1"
    def on_release(self):
        self.pressed = False

class num2(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="2", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "2"
    def on_release(self):
        self.pressed = False

class num3(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="3", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "3"
    def on_release(self):
        self.pressed = False

class num4(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="4", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "4"
    def on_release(self):
        self.pressed = False

class num5(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="5", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "5"
    def on_release(self):
        self.pressed = False
class num6(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="6", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "6"
    def on_release(self):
        self.pressed = False
class num7(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="7", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "7"
    def on_release(self):
        self.pressed = False

class num8(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="8", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "8"
    def on_release(self):
        self.pressed = False

class num9(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="9", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "9"
    def on_release(self):
        self.pressed = False

class multiply(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="x", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "*"
    def on_release(self):
        self.pressed = False

class divide(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="/", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "/"
    def on_release(self):
        self.pressed = False

class add(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="+", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "+"
    def on_release(self):
        self.pressed = False

class subtract(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="-", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        global Value
        Value += "-"
    def on_release(self):
        self.pressed = False

class sqrt(TextButton):
    def __init__(self, game, x=0, y=0, width=25, height=25, text="√", theme=None):
        super().__init__(x, y, width, height, text, theme=None)
        self.game = game

    def on_press(self):
        self.pressed = True
        
    def on_release(self):
        self.pressed = False

class Calculator(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title)
        self.set_location(500,200)
        
        arcade.set_background_color(arcade.color.WHITE)
        self.text = "Graphical User Interface"
        self.text_x = 0
        self.text_y = 300
        self.text_font_size = 40
        self.speed = 1
    
    def set_buttons(self):
        self.button_list.append(num0(self,130,50,75,75))
        self.button_list.append(num1(self,50,350,75,75))
        self.button_list.append(num2(self,130,350,75,75))
        self.button_list.append(num3(self,210,350,75,75))
        self.button_list.append(num4(self,50,250,75,75))
        self.button_list.append(num5(self,130,250,75,75))
        self.button_list.append(num6(self,210,250,75,75))
        self.button_list.append(num7(self,50,150,75,75))
        self.button_list.append(num8(self,130,150,75,75))
        self.button_list.append(num9(self,210,150,75,75))
        self.button_list.append(multiply(self,300,350,75,75))
        self.button_list.append(divide(self,300,250,75,75))
        self.button_list.append(add(self,300,150,75,75))
        self.button_list.append(subtract(self,300,50,75,75))
        self.button_list.append(sqrt(self,210,50,75,75))
        
    def setup(self):
        self.set_buttons()
    
    def on_draw(self):
        arcade.start_render()
        super().on_draw()

    def update(self, delta_time):
        self.speed = -self.speed
        self.text_x += self.speed

def main():
    game = Calculator(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
    
