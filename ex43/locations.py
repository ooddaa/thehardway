from persons import *
from sys import exit
from random import randint
from textwrap import dedent

# from things import *
things = __import__('locations', globals(), locals(), [], 0)


class Location(object):

    def __init__(self, location_name):
        # super().__init__()
        self.location_name = location_name

    # you can enter the location (based on condition)
    def enter(self):
        print(f'Location.enter')

    # and can leave it
    def leave(self, to_location):
        if self.inside == False:
            pass
        else:
            print(f'leaving to {to_location.__class__.__name__}')
            self.inside = False
            return to_location.enter()

    def get_info(self):
        print(self.__class__.__name__)
        pass


class Office(Location):

    def __init__(self):
        super().__init__("Office")

    def get_info(self):
        print(self.__class__.__name__)
        pass


class Morgue(Location):

    def __init__(self):
        super().__init__("Morgue")

    def get_info(self):
        print(self.__class__.__name__)
        info = f"This is morgue, a place where you don't want to be.\nClearly it's a mistake and you say so to the coroner who looks \nas if he's going to have a heart attack. You leave him alone and restart."
        print(info)
        return info

    def restart(self):
        return


morgue = Morgue()


class Roof(Location):

    def __init__(self):
        super().__init__("Roof")
        self.first_time_visit = True
        self.inside = False

    def get_info(self):
        print(self.__class__.__name__)
        return info

    def restart(self):
        return

    def enter(self):
        self.inside = True
        print('You finally got up top to the Roof!\nYou see a helicopter ready to depart.\nWhat\'s your action?.\n\n1. Jump into helicopter.\n2. Return to the office.')
        action = input('Enter option: > ')
        if action == "1":
            print('Yeah! Let\'s rock!')
            return things.helicopter.enter()
        elif action == "2":
            return self.leave()

    def leave(self):
        super().leave(level3)


        # if self.inside == False:
        #     pass
        # else:
        #     print('You cannot leave what you have not entered...')
        #     return level3.enter()
roof = Roof()


class BossOffice(Location):

    def __init__(self):
        super().__init__("BossOffice")
        self.first_time_visit = True
        self.boss_in = bool(randint(0, 1))
        self.inside = False

    def get_info(self):
        print(self.__class__.__name__)
        return info

    def restart(self):
        return

    def enter(self):
        self.inside = True
        if self.boss_in:
            print('You find your Boss in his office.\nHe is looking at you wondering what job to give you whilst you are:\n1. Initiating an escape sequence.\n2. Being frozen.\n3. Start talking.')
            action = input('Enter option: > ')
            if action == "1" or action == "2" or action == "3":
                print('lol, but Im gonna leave anyways')
                self.inside = False
                return level3.enter()
            else:
                print('no such option with boss')
                self.inside = False
                return level3.enter()
        else:
            print('wow boss is not in here, it is a whole different KOLENKOR!')
            self.boss_in = bool(randint(0, 1))
            self.inside = False
            return level3.enter()

    def leave(self):
        if self.inside == False:
            pass
        else:
            print('You cannot leave what you have not entered...')
            self.inside = False
            return level3.enter()


boss_office = BossOffice()


class SecretaryOffice(Location):

    def __init__(self):
        super().__init__("Secretary Office")
        self.first_time_visit = True
        self.inside = False

    def get_info(self):
        print(self.__class__.__name__)
        return info

    def enter(self):
        self.inside = True
        print("hoho, Secretary's office here")
        return

    def restart(self):
        return

    def leave(self):
        if self.inside == False:
            pass
        else:
            print('You cannot leave what you have not entered...')
            self.inside = False
            return level3.enter()


secretary_office = SecretaryOffice()


class HROffice(Location):

    def __init__(self):
        super().__init__("HR Office")
        self.first_time_visit = True
        self.inside = False

    def get_info(self):
        print(self.__class__.__name__)
        return info

    def restart(self):
        return

    def enter(self):
        self.inside = True
        print("hoho, HROffice's office here. WIP")
        return exit(0)

    def leave(self):
        self.inside = False
        return level2.enter()


hr_office = HROffice()

""" Level enters the locations after it makes sure the Door allows it."""


class Level3(Office):

    def __init__(self):
        super().__init__()
        self.level_number = 3
        self.can_leave = False
        self.doors = {
            # [Thing, accessible?]
            '1': [things.secretary_door, False, secretary_office],
            '2': [things.boss_office_door, True, boss_office],
            '3': [things.roof_door, True, roof]
        }
        self.first_time_visit = True

    def enter(self):
        if self.first_time_visit:
            print(
                'You find yourself at Level 3. In front of you are three doors.\nWhich door do you want to try?')
        else:
            print('You are back to Level 3. Choose the door.')

        self.first_time_visit = False
        print(dedent("""Signs on doors say:"""))
        for [num, [door, access, loc]] in self.doors.items():
            print(num, door.get_info())
        door_num = input("> ")

        if door_num == "1" or door_num == "2" or door_num == "3":
            door = self.doors[door_num][0]
            if door.is_accesible == True:
                print(f'You open door {door_num}.')
                return self.doors[door_num][2].enter()
            else:
                # try to unlock
                print(
                    f'Level3: Door {door_num} is locked. Want to try to unlock?')
                ans = input('y/n: ')
                if ans == 'y' or ans == 'yes':
                    door.unlock()
                else:
                    # offer user to enter the level again ie remain at the door
                    return self.enter()
        else:
            print(f'There is no door with number {door_num}')

    def get_info(self):
        # print(self.__class__.__name__)
        info = f'Level number:\t{self.level_number}'
        print(info)
        return info

    def leave(self):
        print(self.__class__.__dict__)
        if self.can_leave:
            print(f'Leaving level {self.level_number}.')
            # return self.previous_location
        else:
            print(f'Cannot leave this level.')
        pass


level3 = Level3()


class Level2(Office):
    level3 = Level3()

    def __init__(self):
        super().__init__()
        self.level_number = 2
        self.can_leave = False
        self.doors = {
            # [Thing, accessible?]
            '1': [things.Door(1, 'Accounting'), False, None],
            '2': [things.hr_door, True, hr_office],
            '3': [things.Door(3, 'Stairs'), True, level3]
        }
        self.first_time_visit = True

    def enter(self):
        if self.first_time_visit:
            print(
                'You find yourself at Level 2. In front of you are three doors.\nWhich door do you want to try?')
        else:
            print('You are back to Level 2. Choose the door.')

        self.first_time_visit = False
        print(dedent("""Signs on doors say:"""))
        for [num, [door, access, loc]] in self.doors.items():
            print(num, door.get_info())
        door_num = input("> ")

        if door_num == "1" or door_num == "2" or door_num == "3":
            if self.doors[door_num][1] == True:
                print(f'You open door {door_num}.')
                return self.doors[door_num][2].enter()
            else:
                print(f'Level2: Door {door_num} is locked.')

    def get_info(self):
        # print(self.__class__.__name__)
        info = f'Level number:\t{self.level_number}'
        print(info)
        return info

    def leave(self):
        print(self.__class__.__dict__)
        if self.can_leave:
            print(f'Leaving level {self.level_number}.')
            # return self.previous_location
        else:
            print(f'Cannot leave this level.')
        pass


level2 = Level2()

""" Uses old mechanism to open doors. Well, uses old Doors. """


class Level1(Office):

    def __init__(self):
        super().__init__()
        self.doors = {
            # [Thing, accessible?, go_through?]
            '1': [things.Door(1, 'Please do not open'), False, morgue],
            '2': [things.Door(2, 'Toilet'), False, None],
            '3': [things.Door(3, 'Stairs'), True, level2]
        }
        self.level_number = 1
        self.can_leave = False
        self.first_time_visit = True

    def enter(self):
        if self.first_time_visit:
            print(dedent("""
            You find yourself at Level 1. In front of you are three doors.
            Which door do you want to try?
            """))
        else:
            print('You are back to Level 1. Choose the door.')

        self.first_time_visit = False
        print(dedent("""Signs on doors say:"""))
        for [num, [door, access, loc]] in self.doors.items():
            print(num, door.get_info())

        door_num = input("> ")

        if door_num == "1" or door_num == "2" or door_num == "3":
            if self.doors[door_num][1] == True:
                print(f'You open door {door_num}.')
                return self.doors[door_num][2].enter()
            else:
                print(f'Level1: Door {door_num} is locked.')
        else:
            print(f'There is no door with number {door_num}')
            self.enter()

    def get_info(self):
        # print(self.__class__.__name__)
        info = f'Level number:\t{self.level_number}'
        print(info)
        return info

    def leave(self):
        print(self.__class__.__dict__)
        if self.can_leave:
            print(f'Leaving level {self.level_number}.')
            # return self.previous_location
        else:
            print(f'Cannot leave this level.')
        pass


level1 = Level1()
