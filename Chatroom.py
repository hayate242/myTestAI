# coding: utf-8


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.graphics import *
# from kivy.uix.GridLayout import GridLayout
from kivy.uix.scrollview import ScrollView

Window.clearcolor = (0.625, 1, 0.80078, 1)

# class CustomWidget(Widget):
#     def__init__(self, **kwargs):
#         super(CustomWidget, self).__init__(**kwargs)
#
#         self.canvas.add(Color(1,1,0))
#         self.canvas.add(Rectangle(size=(self.width,self.height)))
#
#         with self.canvas:
#             Color(0,0,1)
#             Rectangle(size=(250,250),pos=(300,300))


class Chat(FloatLayout):

    # 縦位置調整
    posY = NumericProperty(0)
    # define the multiplication of a function
    def product(self, instance):
        # self.result, self.a and self.b where defined explicitely in the kv
        self.result.text = str(int(self.a.text) * int(self.a.text))

# display the texts here
    def sentText(self, instance):
        self.posY = self.posY+(30/2)
        # self.posY = NumericProperty(self.posY)s
        print(self.posY)
        # self.posY.text += int(30*3/20)
        print("inserted text!")
        s = str(self.a.text)
        # s = s.rstrip()
        s = s.replace('\n','')
        print(s)

        # cntN = 0
        # self.speakerResult.text += '-------------------------\n'
        self.speakerResult.text += 'You: '
        for i in range(0,len(s)):
            self.speakerResult.text += s[i]
            # if i != 0 and i%15 == 0:
            #     self.speakerResult.text += '\n'
            #     self.posY = self.posY+(30/2)
            #     cntN += 1

        self.speakerResult.text += '\n'
        self.speakerResult.text += '-----------------------\n'
        self.posY = self.posY+(30/2)
        # self.add_widget(Label(text="Username:"))

        # self.result.text += '-------------------------\n'
        self.result.text += "野獣先輩: "+"hahaha\n"
        # for i in range(cntN):
        #     self.result.text += "\n"
        self.result.text += '-----------------------\n'

# just for debug
    def reload(self):
        print("Inputbox reloaded")

class TestApp(App):
    icon = 'icon.jpg'
    title = 'ChatBott'


    def build(self):
        self.root = Builder.load_file('root.kv')
        Window.size = (400, 500)
        self.root = Chat()
        # self.root.add_widget(ScrollView())
        return self.root

if __name__ == '__main__':
    TestApp().run()
