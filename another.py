from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
from kivy.animation import Animation
from kivy.uix.button import Button

class CntossBoxLayout(BoxLayout):
    def choice(self,guess):
        output = "Your choice was: "+guess
        self.ids.result.text=output

class CntossApp(App):

    def animate(self, instance):
        animation = Animation(pos=(random.randint(100,300),random.randint(100, 500)), t='out_bounce')
        animation += Animation(pos=(200,100), t='out_bounce')
        animation &= Animation(size=(500,500))
        animation += Animation(size=(100,50))
        animation.start(instance)

    def build(self):
 #       button = Button(size_hint=(None, None), text='plop', on_press=self.animate)
        return CntossBoxLayout()

if __name__ == "__main__":
    CntossApp().run()