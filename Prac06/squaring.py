"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

__author__ = 'Lindsay Ward'


class HBoxWidget(Widget):
    def build(self):
        super(HBoxWidget)


class VBoxWidget(Widget):
    def build(self):
        super(VBoxWidget)


class ContainerBox(BoxLayout):
    def build(self):
        super(ContainerBox)


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Square Number"
        return ContainerBox()

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
