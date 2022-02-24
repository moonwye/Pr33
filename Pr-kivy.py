from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    
    def build(self):
        s=Scatter()
        fl=FloatLayout(size=(200, 200))
        s.add_widget(fl)
        fl.add_widget(Button(
        text="Это кнопка",
        font_size=20,
        on_press=self.btn_press,
        background_color=[1,1,0,1],
        background_normal='',
        size_hint=(.5, .25),
        pos=(10, 20)));
        
        fl.add_widget(Button(
        text="Это кнопка2",
        font_size=20,
        on_press=self.btn_press,
        background_color=[1,1,0,1],
        background_normal='',
        size_hint=(.5, .25),
        pos=(250, 20)));
        return s
    
    def btn_press(self, instance):        
        instance.text='Я нажата'
        
if __name__=="__main__":
    myApp().run()
