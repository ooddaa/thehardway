from sys import exit
from random import randint
from textwrap import dedent
from locations import *
from things import *
from persons import *
# https://docs.python.org/3/tutorial/classes.html


# takes a map and allows playing the map
# moving around it, accessing things, locations, people


class Engine(object):

    def __init__(self, _map):
        self._map = _map

    # returns to previous location
    def step_back(self):
        pass

    def current_location(self):
        return self._map.current_location

    # Starts the map
    def start(self):
        print('The game starts.')
        self._map.current_location = self._map.starting_location
        self._map.current_location.enter()
        return


class Map(object):

    def __init__(self):
        self._map = {
            'office': Office(),
            'level1': Level1(),
            'level2': Level1(),
            'level3': Level1(),
            'roof': Roof(),
            'morgue': Morgue(),
        }
        self.starting_location = self._map['level1']  # to begin with
        self.current_location = None
        self.previous_location = None
        self.location_stack = []

    # def next_location(self):
    #     self.starting_location = _map['level1']
    # allows to see the current map

    def view_map(self):
        pass


mp = Map()
game = Engine(mp)
# mp.starting_location.doors['1'].get_info()
game.start()
# game.current_location().get_info()

# l = Location('here')
# x = Office()
# y = Level(1)
# m = Morgue()
# m.get_info()

# print(x.location_name)
# print(y.location_name, y.level_number)
# y.get_info()
# print(x.get_info())
# y.leave()
# y.can_leave = True
# y.leave()
