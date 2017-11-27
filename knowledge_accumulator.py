from el_scheme import Diod, Transistor, Resistor, Capacitor, Inductance
from frame import Slot


class KnowledgeAccumulator:

    def __init__(self, scheme):
        """
        :type scheme: el_scheme.Scheme
        """
        self._scheme = scheme

    def learning(self):
        """
        Функция извлечения знаний
        """
        menu_text = (
            '1. Вывести список электронных компонентов\n'
            '2. Добавить компонент\n'
            '3. Удалить компонент\n'
            '4. Вывести список контрольных точек\n'
            '5. Добавить контрольную точку\n'
            '6. Удалить контрольную точку\n'
        )

        def print_components():
            self._scheme.print()#_components()

        def print_check_points():
            self._scheme.print()#_check_points()

        menu_methods = [print_components, self.add_component]

        while True:
            self._scheme.print_name()
            print(menu_text)
            menu_method_index = int(input()) - 1
            menu_methods[menu_method_index]()

    def add_component(self, component=None):
        """
        Функция  добавления
        """
        if component is None:
            menu_text = (
                '1. Добавить диод\n'
                '2. Добавить транзистор\n'
                '3. Добавить резистор\n'
                '4. Добавить конденсатор\n'
                '5. Добавить катушку индуктивности\n'
            )
            component_types = [Diod, Transistor, Resistor, Capacitor, Inductance]
            print(menu_text)

            component_type_index = int(input()) - 1
            ComponentType = component_types[component_type_index]

            component = ComponentType()
            for attr_name in dir(component):
                slot = getattr(component, attr_name)
                if isinstance(slot, Slot) and not slot.is_system:
                    print('Введите "{}":'.format(slot.name))
                    slot.value = input()

        self._scheme.add_component(component)

