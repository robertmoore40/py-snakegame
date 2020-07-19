from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from random import randint
from kivy.core.window import Window

class SnakePart(Widget):
    pass



class MainApp(App):
    def on_start(self):
        self.root.new_game()
        Clock.schedule_interval(self.root.next_frame, .25)
    pass


MainApp().run()