from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import random
Builder.load_file('Randomkivy.kv')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '251')
Config.set('graphics', 'height', '100')

class Randomkivy(BoxLayout):
    def press_button_random(self):
        self.text_input.text = str(random.randrange(1, 100))

    def press_button_clear(self):
        self.text_input.text = ''

class RandomApp(App):
    def build(self):
        return Randomkivy()

if __name__ == '__main__':
    RandomApp().run()