from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '290')
Config.set('graphics', 'height', '309')

class MyBoxLayout(BoxLayout):
    def press_btn1(self):
        self.text_input.text += self.button1.text

    def press_btn2(self):
        self.text_input.text += self.button2.text

    def press_result(self):
        self.text_input.text = str(eval(self.text_input.text))

    def press_summ(self):
        self.text_input.text += self.summ.text

class Calculator(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    Calculator().run()