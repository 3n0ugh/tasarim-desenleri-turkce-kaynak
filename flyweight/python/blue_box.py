# Created by Sezer BOZKIR<admin@sezerbozkir.com> at 17.12.2021
from abc import ABC, abstractmethod
from box import Box
from box_color import BoxColor


class BlueBox(Box):
    """
    Flyweight (Box) şablonunu uygulayan sınıftır.
    UML diyagramındaki ConcreteFlyweight sınıfına denk gelmektedir.
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.box_color = BoxColor.Blue

    def draw(self, location_x, location_y):
        print(f"{self.box_color} box drawn. {location_x},{location_y}")
