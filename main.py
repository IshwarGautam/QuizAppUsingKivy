from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'Resizable','0')
Config.set('graphics', 'width', '412')
Config.set('graphics', 'height', '732')

class HomePage(Screen):
    pass
    
class Q1(Screen):
    pass

class Q2(Screen):
    pass

class Q3(Screen):
    pass

class FinalPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

file=Builder.load_file('kivy.kv')

class QuizApp(App):
    def build(self):
        return file

QuizApp().run()
