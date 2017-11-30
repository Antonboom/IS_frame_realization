from frame import Frame, Slot
from frame.slot_types import FramePtrList


class Scheme(Frame):

    _name_ = 'Электрическая схема'
    _slots_ = {
        'IS_A':    (FramePtrList(), Slot.IT_OVERRIDE),
        'PART_OF': (FramePtrList(), Slot.IT_OVERRIDE),

        'elements':     ('Элементы',          FramePtrList(), Slot.IT_UNIQUE),
        'check_points': ('Контрольные точки', FramePtrList(), Slot.IT_UNIQUE),
    }

    def add_component(self, component):
        """
        :type component: el_scheme.Component
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

    def save_to_db(self):
        data = [
            component.serialize()
            for component in self.elements
        ]

        print(data)


