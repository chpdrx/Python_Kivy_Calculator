from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '290')
Config.set('graphics', 'height', '362')

class MyBoxLayout(BoxLayout):
    def press_btn1(self):
        self.text_input.text += self.button1.text

    def press_btn2(self):
        self.text_input.text += self.button2.text

    def press_btn3(self):
        self.text_input.text += self.button3.text

    def press_btn4(self):
        self.text_input.text += self.button4.text

    def press_btn5(self):
        self.text_input.text += self.button5.text

    def press_btn6(self):
        self.text_input.text += self.button6.text

    def press_btn7(self):
        self.text_input.text += self.button7.text

    def press_btn8(self):
        self.text_input.text += self.button8.text

    def press_btn9(self):
        self.text_input.text += self.button9.text

    def press_btn0(self):
        self.text_input.text += self.button0.text

    def press_result(self):
        if type(eval(self.text_input.text)) == float and eval(self.text_input.text)%1==0:
            self.text_input.text = str(int(eval(self.text_input.text)))
        else:
            self.text_input.text = str(eval(self.text_input.text))

    def press_summ(self):
        self.text_input.text += self.summ.text

    def press_sub(self):
        self.text_input.text += self.sub.text

    def press_multi(self):
        self.text_input.text += self.multi.text

    def press_div(self):
        self.text_input.text += self.div.text

    def press_clear(self):
        self.text_input.text = ''

class Calculator(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    Calculator().run()