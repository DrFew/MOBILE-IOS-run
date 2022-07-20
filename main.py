import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '780')

Builder.load_file('MobileAPP.kv')

class MobileAPP(Widget):

    def add1 (self):
        self.ids.Item1.text = str(int(self.ids.Item1.text) + 1 )
        self.Sum_text()

    def sub1 (self):
        if int(self.ids.Item1.text) > 0 :
            self.ids.Item1.text = str(int(self.ids.Item1.text) - 1 )
            self.Sum_text()

    def add2 (self):
        self.ids.Item2.text = str(int(self.ids.Item2.text) + 1 )
        self.Sum_text()

    def sub2 (self):
        if int(self.ids.Item2.text) > 0 :
            self.ids.Item2.text = str(int(self.ids.Item2.text) - 1 )
            self.Sum_text()

    def reset (self):
        self.ids.Item1.text = '0'
        self.ids.Item2.text = '0'   
        self.Sum_text()

    def Sum_text (self):
        self.ids.Sum.text = str(int(self.ids.Item1.text) + int(self.ids.Item2.text))
    
class MainApp(App):
    def build(self):
        return MobileAPP()
if __name__ == '__main__':
    MainApp().run()

