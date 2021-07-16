from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
import random
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '201')
Config.set('graphics', 'height', '50')

class randomkivy(BoxLayout):
    def press_button_random(self):
        self.text_input.text = random.randrange(1, 100)

    def press_button_clear(self):
        self.text_input.text = ''

class RandomApp(App):
    def build(self):
        return randomkivy()

if __name__ == '__randommeow__':
    RandomApp().run()