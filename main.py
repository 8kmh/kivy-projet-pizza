from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()

class MainWidget(BoxLayout):
    recycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Pizzas = [
            Pizza("4 fromages", "chèvre, emmental, brie, comté", 9.5, True),
            Pizza("Chorizo", "tomates, chorizo, parmesan", 11.2, False),
            Pizza("Calzone", "fromage, jambon, champignons", 10, False),
        ]

    def on_parent(self, widget, parent):
        self.recycleView.data = [
            {"nom": "4 fromages"},
            {"nom": "Chorizo"}
        ]


class PizzaApp(App):
    pass


PizzaApp().run()