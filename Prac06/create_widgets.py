
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class LabelCreatorApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.labels = ['a', 'b', 'c', 'd', 'e', 'f']

    def build(self):
        self.root = Builder.load_file('create_widgets.kv')
        self.create_widgets(self.labels)
        return self.root

    def create_widgets(self, labels_string):
        for string in labels_string:
            temp_label = Label(text=string)
            self.root.ids.widgetsBox.add_widget(temp_label)

LabelCreatorApp().run()
