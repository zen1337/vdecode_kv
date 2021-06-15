import win32clipboard
import time
import base64

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='btn 1'))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)
        self.add_widget(Button(text='btn 2'))
        cb2 = CustomBtn2()
        cb2.bind(pressed=self.btn_pressed)
        self.add_widget(cb2)

    def btn_pressed(self, instance, pos):
        print ('pos: printed from root widget: {pos}'.format(pos=pos))

class CustomBtn2(Widget):

    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
             # we consumed the touch. return False here to propagate
             # the touch further to the children.
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        while True:
            time.sleep(1)
            try:
                win32clipboard.OpenClipboard()
            except:
                print("open clip failed bruh")
                continue

            try:
                data = win32clipboard.GetClipboardData()
                print(data)
                if data:
                    data = data.encode("utf-8")
                    print(data)
                    datax = win32clipboard.SetClipboardText(base64.b64encode(data))
                    print(datax)
                    win32clipboard.CloseClipboard()
                else:
                    break
            except Exception as ex:
                print(ex)
                continue

class CustomBtn(Widget):

    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
             # we consumed the touch. return False here to propagate
             # the touch further to the children.
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print ('pressed at {pos}'.format(pos=pos))

class TestApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()