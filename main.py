from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from random import randint
from kivy.core.window import Window

class SnakePart(Widget):
    pass

class GameScreen(Widget):
    step_size = 40
    movement_x = 0
    movement_y = 0
    snake_parts = []

    def new_game(self):
        to_be_removed = []
        for child in self.children:
            if isinstance(child, SnakePart):
                to_be_removed.append(child)
        for child in to_be_removed:
            self.remove_widget(child)

             self.snake_parts = []
        self.movement_x = 0
        self.movement_y = 0
        head = SnakePart()
        head.pos = (0, 0)
        self.snake_parts.append(head)
        self.add_widget(head)



class MainApp(App):
    def on_start(self):
        self.root.new_game()
        Clock.schedule_interval(self.root.next_frame, .25)
    pass


MainApp().run()