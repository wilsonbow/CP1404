
__author__ = 'Wilson Bow'

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConversionApp(App):

    def build(self):
        Window.size = (300, 200)
        self.title = "Miles to kilometres converter"
        self.root = Builder.load_file('miles_km.kv')
        return self.root

    def handle_convert(self, miles_input):
        kilometres = miles_input / 1.609344
        self.root.ids.output.text = str(kilometres)

    def handle_increment(self, current_value, increment_value):
        new_value = current_value + increment_value
        self.root.ids.input.text = str(new_value)

ConversionApp().run()