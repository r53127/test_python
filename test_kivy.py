from kivy.app import App
from kivy.event import EventDispatcher
from kivy.uix.label import Label
from kivy.uix.popup import Popup
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
        cb.bind(on_swipe=self.on_swipe_callback)
        cb.dispatch('on_swipe')
        self.add_widget(cb)
        self.add_widget(Button(text='btn 2'))


    def on_swipe_callback(*largs):
        print('我的swipe被调用', largs)

    def btn_pressed(self, instance, pos):
        print('pos: printed from root widget: {pos}'.format(pos=pos))


class CustomBtn(Widget):
    pressed = ListProperty([0, 0])
    def __init__(self, **kwargs):
        super(CustomBtn, self).__init__(**kwargs)
        self.register_event_type('on_swipe')
    def on_swipe(self):
        pass


    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print('当前监控位置：',touch.pos)
            self.pressed = touch.pos
            print('prssed位置：',type(self.pressed),self.pressed)
            # we consumed the touch. return False here to propagate

        # the touch further to the children.
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self,instance,pos):
        print('pressed at {0},{1},{2}'.format(pos,instance,self))


class TestApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def build(self):
        a=RootWidget()
        return a


if __name__ == '__main__':
    TestApp().run()
