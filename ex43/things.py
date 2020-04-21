from sys import exit
from random import randint
from textwrap import dedent

# from locations import *
from persons import *

locations = __import__('locations', globals(), locals(), [], 0)


class Thing(object):

    def __init__(self):
        pass

    def get_info(self):
        print(self.__class__.__name__)
        pass


class Door(Thing):
    def __init__(self, number, info=''):
        self.door_number = number
        self.info = info
        self.is_accesible = False

    def get_info(self):
        # print(self.__class__.__name__)
        return self.info

    def get_door_number(self):
        return self.door_number

    """ To unlock a door, we need to get some job done. 
    Door has a list of a notepad paper saying what the challenge is. 
    @todo add random challenges. 
    """

    def unlock(self):
        print(
            dedent(f"""You are trying to unlock door {self.get_door_number()}."""))
        task = self.task_to_unlock_door()
        if task == True:
            self.is_accesible = True
            print(f'Yay, the door is now open!')
            return self.enter()
        else:
            print(f'Hmm, you should try next time.')

    def enter(self):
        if self.is_accesible == False:
            print(f'Door: The door is locked!')
            return self  # return to appropriate level self.remain_where_you_are() ??!?
        else:
            return self.go_through()
            # return self.go_through().enter() # this won't work as context is lost??

    def task_to_unlock_door(self):
        # genering unlocking task - just knocknock
        print(f'Knock knock')
        # sometimes it will miraculously open
        if randint(1, 100) <= 50:
            print(f'Wow, a miracle has just opened the door!')
            self.is_accesible == True
            return True
        else:
            print(f'Door: The door is still locked!')
            return False


class SecretaryDoor(Door):
    def __init__(self):
        super().__init__(1, 'Secretary door')

    def task_to_unlock_door(self):
        print(f'2 + 2 = ?')
        ans = input("> ")
        if ans == "4":
            return True
        else:
            return False

    def enter(self):
        return locations.secretary_office.enter()

    def stay(self):
        return locations.level3.enter()


class BossOfficeDoor(Door):
    def __init__(self):
        super().__init__(2, 'Boss Office door')

    def task_to_unlock_door(self):
        print(f'0 + 0 = ?')
        ans = input("> ")
        """ add self.isaccessible = 1 here, or abstract this part to parent class? """
        # return self.examinator(ans == "0")
        if ans == "0":
            return True
        else:
            return False

    def enter(self):
        return locations.boss_office.enter()

    def stay(self):
        return locations.level3.enter()


class HRDoor(Door):
    def __init__(self):
        super().__init__(2, 'HR door')

    def task_to_unlock_door(self):
        print(f'3 + 1 = ?')
        ans = input("> ")
        if ans == "4":
            return True
        else:
            return False

    def enter(self):
        return locations.hr_office.enter()

    def stay(self):
        return locations.level2.enter()


class RoofDoor(Door):
    def __init__(self):
        super().__init__(3, 'Roof door')

    def task_to_unlock_door(self):
        print(f'3 + 0 = ?')
        ans = input("> ")
        if ans == "3":
            return True
        else:
            return False

    def enter(self):
        return locations.roof.enter()

    def stay(self):
        return locations.level3.enter()


class Helicopter(Thing):
    def __init__(self):
        pass

    def enter(self):
        print('You have won!')
        exit(0)


secretary_door = SecretaryDoor()
boss_office_door = BossOfficeDoor()
hr_door = HRDoor()
roof_door = RoofDoor()
helicopter = Helicopter()
