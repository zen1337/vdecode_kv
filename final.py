from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import clipboard
import base64


class VdecodeBoxLayout(BoxLayout):
    def choice(self, pick):
        output = pick + " Function have been enabled"
        self.ids.func.text = output

    def buttonEnabled(self,id):
        x = id
        enable = (2,2,2,2)
        disable = (1,1,1,1)
#        y = clipboard.paste()
#        print(y)
        if x == "b1":
            self.ids.b1.background_color = enable
            self.ids.b2.background_color = disable
            self.ids.b3.background_color = disable
 #           y = clipboard.paste()
  #          self.b64dec(y)
            self.b64dec()
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

#    def b64dec(self, text):
    def b64dec(self):
        clpOld = ""
        clp =  clipboard.paste()
        while True:
            try:
                clp = bytes(text, 'utf-8')
                clp = base64.decode(clp)
                clp = bytes.decode(clp)
                clipboard.copy(clp)
            except:
                continue

"""        text = bytes(text, 'utf-8')
        encode = base64.b64encode(text)
        decode2 = base64.b64decode(text)
        print(bytes.decode(decode))
        print(bytes.decode(encode))
        decode2 = bytes.decode(decode2)
        clipboard.copy(decode2)
        final = decode2
        print(decode2)
"""
    def vdec(self, text):
        pass

    def KMSdec(self, text):
        pass

class VdecodeApp(App):
#    pass
    def build(self):
        return VdecodeBoxLayout()
if __name__ == "__main__":
    VdecodeApp().run()