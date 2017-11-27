from frame import Frame, Slot
from frame.slot_types import FramePtrList


class Scheme(Frame):

    _name_ = 'Электрическая схема'
    _slots_ = {
        'IS_A':    None,
        'PART_OF': None,

        'elements':     ('Элементы',          FramePtrList, Slot.IT_UNIQUE),
        'check_points': ('Контрольные точки', FramePtrList, Slot.IT_UNIQUE),
    }

    def add_component(self, component):
        """
        :type component: Component
        """
        self.elements.append(component)

    def print(self):
        for element in self.elements:
            print(element)
        print()

        for point in self.check_points:
            print(point)

    def print_name(self):
        print(self.title)
