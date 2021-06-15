from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ActionBoxLayout(BoxLayout):
    def choice(self, pick):
        output = pick + " Function have been enabled"
        self.ids.func.text = output

    def buttonEnabled(self,id):
        x = id
        enable = (2,2,2,2)
        disable = (1,1,1,1)
#        print(id)
        if x == "b1":
            self.ids.b1.background_color = enable
            self.ids.b2.background_color = disable
            self.ids.b3.background_color = disable

        elif x == "b2":
            self.ids.b2.background_color = enable
            self.ids.b1.background_color = disable
            self.ids.b3.background_color = disable
        elif x == "b3":
            self.ids.b3.background_color = enable
            self.ids.b1.background_color = disable
            self.ids.b2.background_color = disable
        else:
            pass
class ActionApp(App):
#    pass
    def build(self):
        return ActionBoxLayout()
if __name__ == "__main__":
    ActionApp().run()