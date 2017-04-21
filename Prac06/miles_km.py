
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
        try:
            miles_float = float(miles_input)
        except ValueError:
            miles_float = 0
        kilometres = miles_float / 1.609344
        self.root.ids.input.text = str(miles_float)
        self.root.ids.output.text = str(kilometres)

    def handle_increment(self, current_value, increment_value):
        new_value = current_value + increment_value
        self.root.ids.input.text = str(new_value)

ConversionApp().run()