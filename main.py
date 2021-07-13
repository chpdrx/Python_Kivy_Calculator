from kivy.app import App
from kivy.uix.button import Button

class Calculator(App):
    x = 0
    def build(self):
        b1 = Button(text = '1', font_size = 20)
        b1.background_color = [0,1,0,1]
        b1.bind(on_press = callback)
        return b1

    def callback(self):
        return b1.text

    def calculator(self, callback(), y, z):
        return eval(x + z + y)

if __name__ == '__main__':
    Calculator().run()